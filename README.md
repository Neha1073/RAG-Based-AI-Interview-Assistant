# RAG-Based-AI-Interview-Assistant

## 🚀 Overview

This project implements a Retrieval-Augmented Generation (RAG) system that answers AI/ML interview questions using custom notes.

It combines:

* Vector search (FAISS)
* Embeddings (sentence-transformers)
* Local LLM (Ollama)

---

## 🧠 Features

* Ask questions from AI/ML syllabus
* Retrieves relevant notes
* Generates grounded answers
* Supports local LLM (no API cost)

---

## 🏗️ Tech Stack

* Python
* FAISS
* LangChain
* Sentence Transformers
* Ollama

---

## 📂 Project Structure

rag-project/
│── rag_app.py
│── notes/
│── requirements.txt

---

## ⚙️ Setup Instructions

### 1. Clone repo

git clone <your-repo-link>
cd rag-project

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run Ollama

ollama run phi

### 4. Run project

python rag_app.py

---

## 💡 Example

Question: What is overfitting?
Answer: Model memorizes training data but fails to generalize.

---

## 🔥 Future Improvements

* Add evaluation using RAGAS
* Hybrid search (BM25 + FAISS)
* Web UI (Streamlit)

---

## 🎯 Use Case

* AI/ML interview preparation
* Concept revision assistant
