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

├── README.md
├── __pycache__
│   ├── chroma_client.cpython-312.pyc
│   ├── config.cpython-312.pyc
│   ├── document_loader.cpython-312.pyc
│   ├── embedding_function.cpython-312.pyc
│   ├── embedding_manager.cpython-312.pyc
│   ├── embedding_model.cpython-312.pyc
│   └── query_helper.cpython-312.pyc
├── chroma
│   └── chroma.sqlite3
├── chroma_client.py
├── config.py
├── data
├── document_loader.py
├── embedding_manager.py
├── embedding_model.py
├── generate_embedding.py
├── main.py
├── notebooks
│   ├── chroma_db.ipynb
│   └── document.ipynb
├── query_helper.py
├── requirements.txt
└── vector_store
    ├── 51df7c47-b390-4cc9-9eb7-41fd3c46ed4a
    │   ├── data_level0.bin
    │   ├── header.bin
    │   ├── index_metadata.pickle
    │   ├── length.bin
    │   └── link_lists.bin
    └── chroma.sqlite3

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