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

This project demonstrates a practical implementation of Retrieval-Augmented Generation using local models. It ensures accurate, explainable, and document-grounded responses, making it suitable for applications like policy assistants, document Q&A systems, and internal knowledge bases.
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)
![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)
![alt text](image-9.png)