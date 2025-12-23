# 📄 Resume-Based AI Chatbot (RAG)

A **Resume-Based AI Chatbot** built using **Retrieval-Augmented Generation (RAG)** that allows users to ask questions about a resume and receive accurate, context-aware answers grounded strictly in the resume content.

This project is useful for **resume screening, personal portfolios, and interview preparation**.

---

## 🚀 Features

- 📤 Upload and process resumes (PDF/Text)
- 🔍 Semantic search over resume content
- 💬 Natural language Q&A
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Accurate responses based only on resume data

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Vector Database (FAISS / Chroma)**
- **OpenAI / LLM API**
- **VS Code**
- **Git & GitHub**

---

## 🧠 How It Works

1. Resume is loaded and split into chunks  
2. Text chunks are converted into embeddings  
3. Embeddings are stored in a vector database  
4. User query retrieves relevant chunks  
5. LLM generates an answer using retrieved context  


