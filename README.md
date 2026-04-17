# 🚀 Retrieval-Augmented Generation (RAG) Pipeline

A modular and scalable implementation of a **Retrieval-Augmented Generation (RAG)** system built from scratch using **ChromaDB** and **Sentence Transformers**. This project demonstrates end-to-end pipeline design, including document ingestion, embedding generation, vector storage, and semantic retrieval.

---

## 📌 Overview

This project implements a **RAG-based architecture** for efficient semantic search and context-aware retrieval from unstructured PDF data.

It is designed with a focus on:
- Clean and maintainable architecture
- Scalability for production use cases
- Easy integration with LLM-based systems (chatbots, AI agents)

---

## 🛠️ Tech Stack

- **Vector Database:** ChromaDB  
- **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`  
- **Programming Language:** Python  
- **Environment Management:** uv  
- **Data Source:** PDF documents  

---

## ⚙️ Project Setup

### 1. Create Virtual Environment & Install Dependencies

```bash
uv venv
uv pip install -r requirements.txt
```

---

### 2. Configure Environment Variables

Copy `.env.example` and create a `.env` file:

| Variable           | Description                                      |
|------------------|--------------------------------------------------|
| COLLECTION_NAME  | Name of the ChromaDB collection                  |
| CHROMA_DB_PATH   | Path for persistent vector database              |
| EMBEDDING_MODEL  | Embedding model name                             |
| PDF_PATH         | Path or URL of the input PDF document            |

---

## 🔄 Pipeline Architecture

### 1. Ingestion Pipeline (Embedding Generation)

Responsible for:
- Loading and parsing PDF documents  
- Splitting content into chunks  
- Generating embeddings using Sentence Transformers  
- Storing vectors in ChromaDB  

📄 **Entry Point:** `generate_embedding.py`

---

### 2. Retrieval Pipeline (Semantic Search)

Responsible for:
- Accepting user queries  
- Generating query embeddings  
- Performing similarity search on stored vectors  
- Returning relevant document chunks  

📄 **Entry Point:** `main.py`

---

## ✨ Key Features

- 🔍 Semantic search using dense vector embeddings  
- ⚡ Fast and efficient retrieval with ChromaDB  
- 🧠 Optimized text chunking strategy  
- 🧩 Modular and extensible architecture  
- 🔒 Environment-based configuration management  

---

## 📈 Use Cases

- AI-powered document search systems  
- Knowledge base assistants  
- Interview preparation tools  
- Enterprise document retrieval systems  
- RAG-based AI agents  

---

## 🚀 Future Enhancements

- Integration with LLMs for complete RAG responses  
- Support for multiple document formats (DOCX, HTML, etc.)  
- Hybrid search (keyword + semantic)  
- API layer for production deployment  
- Real-time/streaming response support  

---

## 📂 Project Structure

```
.
├── generate_embedding.py   # Ingestion pipeline
├── main.py                 # Retrieval pipeline
├── requirements.txt
├── .env.example
└── README.md
```

---

## ▶️ How to Run

### Step 1: Generate Embeddings
```bash
python generate_embedding.py
```

### Step 2: Run Semantic Search
```bash
python main.py
```