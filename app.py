import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tempfile

st.set_page_config(page_title="AI Policy Assistant", layout="wide")

st.markdown("""
<style>
.chat-container {max-width: 850px; margin: auto;}
.user-msg {
    background: linear-gradient(135deg, #2563eb, #1e40af);
    padding: 12px; border-radius: 12px; margin: 8px;
    color: white; text-align: right;
}
.bot-msg {
    background-color: #1f2937;
    padding: 12px; border-radius: 12px; margin: 8px;
    color: #e5e7eb; text-align: left;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center;'>AI Policy Chatbot</h2>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if "messages" not in st.session_state:
    st.session_state.messages = []

if "db" not in st.session_state:
    st.session_state.db = None

if "llm" not in st.session_state:
    st.session_state.llm = OllamaLLM(model="phi3")

if "stop_generation" not in st.session_state:
    st.session_state.stop_generation = False

if "current_response" not in st.session_state:
    st.session_state.current_response = ""

if "is_generating" not in st.session_state:
    st.session_state.is_generating = False

@st.cache_resource(show_spinner=False)
def process_pdf(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_bytes)
        path = tmp.name

    docs = PyPDFLoader(path).load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=350,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(chunks, embeddings)
    return db

if uploaded_file and st.session_state.db is None:
    with st.spinner("Processing document..."):
        st.session_state.db = process_pdf(uploaded_file.getvalue())
    st.success("Document ready")

col1, col2 = st.columns([6, 1])
with col2:
    if st.button("Stop"):
        st.session_state.stop_generation = True
        st.session_state.is_generating = False

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"<div class='user-msg'>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{msg}</div>", unsafe_allow_html=True)

# show partial answer after stop
if st.session_state.current_response and not st.session_state.is_generating:
    st.markdown(
        f"<div class='bot-msg'>{st.session_state.current_response}</div>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

query = st.chat_input("Ask your question...")

if query:
    st.session_state.stop_generation = False
    st.session_state.is_generating = True
    st.session_state.current_response = ""

    st.session_state.messages.append(("user", query))
    st.markdown(f"<div class='user-msg'>{query}</div>", unsafe_allow_html=True)

    if st.session_state.db:

        docs = st.session_state.db.similarity_search(query, k=3)

        if not docs:
            answer = "No relevant information found."
            st.session_state.messages.append(("bot", answer))
            st.rerun()

        context = "\n\n".join([d.page_content for d in docs])
        context = context[:1500]

        prompt = f"""
You are an AI assistant.

Use the provided context to answer the question clearly.
Extract exact rules, values, or explanations.

If the answer is not present, say: Not available in document.

Context:
{context}

Question:
{query}

Answer:
"""

        placeholder = st.empty()

        for chunk in st.session_state.llm.stream(prompt):

            if st.session_state.stop_generation:
                break

            st.session_state.current_response += chunk

            placeholder.markdown(
                f"<div class='bot-msg'>{st.session_state.current_response}▌</div>",
                unsafe_allow_html=True
            )

        st.session_state.is_generating = False

        placeholder.markdown(
            f"<div class='bot-msg'>{st.session_state.current_response}</div>",
            unsafe_allow_html=True
        )

        answer = st.session_state.current_response

        with st.expander("Source from document"):
            for i, doc in enumerate(docs):
                st.markdown(f"Chunk {i+1}")
                st.write(doc.page_content[:300])

    else:
        answer = "Please upload document first."

    st.session_state.messages.append(("bot", answer))
    st.rerun()
