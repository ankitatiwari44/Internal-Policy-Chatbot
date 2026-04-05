# AI Policy Chatbot using RAG

## Overview

This project is an AI-powered chatbot designed to answer questions based strictly on a provided policy document. It uses a Retrieval-Augmented Generation (RAG) approach to ensure that all responses are grounded in the uploaded document and not based on external knowledge.

The system allows users to upload a PDF document and interact with it through natural language queries. The chatbot retrieves relevant sections of the document and generates accurate responses using a local language model.

---

## Features

* Document-based question answering
* Uses Retrieval-Augmented Generation (RAG)
* Local inference using Ollama (no external API required)
* Fast response with optimized retrieval and context handling
* Streaming response for better user experience
* Source highlighting for transparency
* Clean chat-based user interface using Streamlit

---

## How It Works

### 1. Document Upload

The user uploads a PDF document through the interface. The system processes the document and prepares it for querying.

### 2. Text Processing

* The document is split into smaller chunks using a text splitter
* Each chunk is converted into vector embeddings using a sentence transformer model

### 3. Vector Database

* All embeddings are stored in a FAISS vector database
* This enables efficient similarity-based retrieval

### 4. Query Handling

When a user asks a question:

* The system searches for the most relevant chunks using similarity search
* Top matching chunks are selected as context

### 5. Response Generation

* The retrieved context is passed to a local language model (via Ollama)
* The model generates an answer strictly based on the provided context

### 6. Source Display

* The system also shows the relevant document chunks used to generate the answer
* This improves transparency and trust in responses

---

## Agent Behavior

The chatbot behaves as a document-grounded assistant with the following characteristics:

* Answers only from the provided document context
* Does not use external or prior knowledge
* Returns "Not available in document" if the answer is not found
* Extracts and summarizes key information from relevant sections
* Handles rephrased and natural language queries effectively

---

## Tech Stack

* Frontend: Streamlit
* LLM Runtime: Ollama
* Language Model: phi3
* Embeddings: sentence-transformers (MiniLM)
* Vector Database: FAISS
* Document Loader: PyPDFLoader
* Text Splitting: RecursiveCharacterTextSplitter

---

## Installation

1. Install dependencies:

```bash
pip install streamlit langchain langchain-community langchain-ollama sentence-transformers faiss-cpu
```

2. Install and run Ollama:

* Download from: https://ollama.com
* Pull model:

```bash
ollama pull phi3
```

---

## Running the Application

```bash
streamlit run app.py
```

---

## Usage

1. Upload a PDF document
2. Wait for processing to complete
3. Ask questions related to the document
4. View answers along with source context

---

## Limitations

* Answers depend entirely on the uploaded document
* Performance may vary based on system hardware
* Large documents may increase processing time
* Local models may have limited reasoning compared to cloud-based models

---

## Future Improvements

* Add conversational memory for follow-up questions
* Highlight exact answers in source text
* Add confidence scoring
* Support multiple documents
* Improve ranking using hybrid search

---

## Conclusion

This project demonstrates a practical implementation of Retrieval-Augmented Generation using local models. It ensures accurate, explainable, and document-grounded responses, making it suitable for applications like pol
icy assistants, document Q&A systems, and internal knowledge bases.
<img width="1920" height="893" alt="image" src="https://github.com/user-attachments/assets/0675c01b-d598-47a7-90df-cce780aa1dc2" />
<img width="1462" height="737" alt="image-1" src="htt<img width="1333" height="802" alt="image-5" src="https://github.com/user-attachments/assets/be2b1c74-5f75-4fe4-80c6-5e1105bab667" />
<img width="1461" height="825" alt="image-2" src="https://github.com/user-attachments/assets/b384e289-d179-4a23-bba0-6d022b3a185b" />
<img width="1424" height="794" alt="image-3" src="https://github.com/user-attachments/assets/c1349420-ab1c-4fbc-840d-fdbf42bab334" />
ps://git<img width="1412" height="747" alt="image-4" src="https://github.com/user-attachments/assets/80f88974-af0d-420d-bde3-993873dc9033" />
<img width="1333" height="802" alt="image-5" src="https://github.com/user-attachments/assets/e62d8cc0-2d9f-4f14-b0aa-b2b7e3117d6c" />
hub.com/user-attachments/assets/635c1f4b-ddf1-442c-af5b-bec59738d3<img width="1326" height="592" alt="image-6" src="https://github.com/user-attachments/assets/802880c1-7b65-4bac-80a0-de55c7d14ea3" />
c3" /><img width="1433" height="567" alt="image-7" src="https://github.com/user-attachments/assets/75a4ad7b-f430-4f33-b9fb-c3e07c694392" />
<img width="1428" height="732" alt="image-8" src="https://github.com/user-attachments/assets/0063e05b-2c00-4846-b646-5712fc71edc1" />
<img width="1309" height="709" alt="image-9" src="https://github.com/user-attachments/assets/d2ede405-111c-447e-9e8d-3affe8bae6cc" />


