# 📄 DocuTrace

### Multi-Hop Document Intelligence with Verifiable Citation Chains

> **An enterprise-inspired Agentic Retrieval-Augmented Generation (RAG) system that answers questions from documents through multi-step reasoning, evidence aggregation, citation verification, and automated evaluation.**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20Workflow-success)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/Vector%20Store-FAISS-orange)
![Phi-3](https://img.shields.io/badge/LLM-Phi--3-purple)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## 📖 Overview

Large documents such as research papers, technical reports, legal documents, and business reports often contain valuable information that is difficult to locate quickly. Traditional document question-answering systems typically retrieve relevant text but provide limited transparency into how an answer was produced or whether it is supported by evidence.

**DocuTrace** is a document intelligence system that demonstrates how an Agentic RAG workflow can improve transparency and trustworthiness in document question answering.

Instead of relying on a single retrieval and generation step, DocuTrace uses a modular workflow that plans the query, retrieves relevant evidence, generates an answer grounded in the retrieved context, performs answer reflection, verifies the response, and reports evaluation metrics to help users assess answer quality.

The system also provides an interactive Streamlit dashboard where users can explore retrieved evidence, inspect supporting sources, review evaluation metrics, and understand the reasoning process behind generated responses.

---

## ⭐ Why DocuTrace?

DocuTrace was developed to explore how modern Retrieval-Augmented Generation (RAG) systems can produce answers that are not only relevant but also transparent and verifiable.

The project focuses on:

* Improving transparency through evidence-grounded responses.
* Demonstrating a modular multi-agent workflow using LangGraph.
* Providing citation-aware document question answering.
* Evaluating answer quality using faithfulness, answer relevancy, context precision, and context recall.
* Presenting the complete reasoning pipeline through an interactive dashboard.


---

# ✨ Key Features

## 🤖 Agentic RAG Workflow

* Multi-agent workflow orchestrated using **LangGraph**.
* Query decomposition through a dedicated **Planner Agent**.
* Answer generation using a local **Phi-3** Large Language Model via **Ollama**.
* Reflection stage for answer refinement before final verification.

## 🔍 Retrieval & Evidence

* Hybrid retrieval pipeline combining semantic retrieval with keyword-based retrieval.
* FAISS vector database for efficient similarity search.
* Evidence aggregation from retrieved document chunks.
* Source-aware responses with document citations.

## 📊 Evaluation & Verification

* Automated answer verification.
* Faithfulness evaluation.
* Answer relevancy evaluation.
* Context Precision and Context Recall metrics.
* Transparent reasoning and evaluation dashboard.

## 🖥️ Interactive Dashboard

* Modern Streamlit interface with modular architecture.
* Interactive Insights Panel.
* Evidence Aggregation Viewer.
* Retrieved Sources Explorer.
* Documents Information Page.
* About Project Page.

---

## 📦 Current Release

**Version:** `v1.0`

### Implemented

- ✅ Modular Streamlit Dashboard
- ✅ Multi-Agent LangGraph Workflow
- ✅ Hybrid Retrieval Pipeline
- ✅ Evidence Aggregation
- ✅ Citation Verification
- ✅ Reflection-based Answer Refinement
- ✅ Faithfulness & Relevancy Evaluation
- ✅ Interactive Insights Panel


---

# 🏗️ System Architecture

DocuTrace follows a modular Agentic Retrieval-Augmented Generation (RAG) architecture where each stage of the pipeline is responsible for a specific task. Instead of directly generating responses from retrieved text, the workflow separates planning, retrieval, generation, reflection, verification, and evaluation into independent components.

```text
                     User Query
                          │
                          ▼
                  Planner Agent
                          │
                          ▼
              Hybrid Retrieval Pipeline
             (Semantic + Keyword Search)
                          │
                          ▼
               Evidence Aggregation
                          │
                          ▼
                 Generator Agent
                   (Phi-3 via Ollama)
                          │
                          ▼
                 Reflection Agent
                          │
                          ▼
              Citation Verification
                          │
                          ▼
             Evaluation Pipeline
      • Faithfulness
      • Answer Relevancy
      • Context Precision
      • Context Recall
                          │
                          ▼
                Final Response
                          │
                          ▼
            Interactive Streamlit UI
```

### Workflow Components

| Component             | Responsibility                                                                                                   |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Planner Agent         | Analyzes the user query and prepares the reasoning workflow.                                                     |
| Hybrid Retrieval      | Retrieves the most relevant document chunks using semantic and keyword-based retrieval.                          |
| Evidence Aggregation  | Combines retrieved context into a unified evidence set.                                                          |
| Generator Agent       | Generates an answer grounded in the retrieved evidence using Phi-3.                                              |
| Reflection Agent      | Reviews the generated answer before verification.                                                                |
| Citation Verification | Ensures citations correspond to retrieved evidence.                                                              |
| Evaluation Pipeline   | Computes answer quality metrics including faithfulness, answer relevancy, context precision, and context recall. |
| Streamlit Dashboard   | Presents answers, evidence, evaluation metrics, and retrieved sources through an interactive interface.          |


---

# 🛠️ Tech Stack

| Category                       | Technologies                    |
| ------------------------------ | ------------------------------- |
| **Programming Language**       | Python                          |
| **Frontend**                   | Streamlit, Custom CSS           |
| **AI Orchestration**           | LangGraph                       |
| **RAG Framework**              | LangChain                       |
| **Large Language Model (LLM)** | Phi-3 (via Ollama)              |
| **Embeddings**                 | Sentence Transformers           |
| **Vector Database**            | FAISS                           |
| **Retrieval**                  | Hybrid Retrieval (FAISS + BM25) |
| **Document Processing**        | PyMuPDF                         |
| **Model Hub**                  | Hugging Face Hub                |
| **Evaluation**                 | DeepEval                        |
| **Machine Learning**           | Scikit-learn                    |
| **Development Environment**    | Visual Studio Code              |


---

# 📂 Project Structure

```text
DocuTrace/
│
├── app/
│   ├── agents/              # LangGraph workflow nodes
│   ├── evaluation/          # Faithfulness & relevancy evaluation
│   ├── ingestion/           # Document loading & preprocessing
│   ├── ml/                  # Embeddings & ML utilities
│   ├── rag/                 # RAG pipeline
│   ├── retrieval/           # Hybrid Retrieval & reranking
│   ├── services/            # Backend service layer
│   └── verification/        # Citation verification
│
├── data/                    # Source documents & vector database
│
├── frontend/
│   ├── assets/              # Images & static assets
│   ├── components/          # Dashboard components
│   ├── pages/               # About & Documents pages
│   ├── main.py              # Streamlit entry point
│   ├── run_frontend.py
│   └── styles.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE (Planned)
```

---

## 📖 Directory Overview

| Directory         | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| **app/**          | Core backend implementation of the Agentic RAG workflow.                     |
| **agents/**       | Planner, Generator, Reflection and other workflow nodes.                     |
| **retrieval/**    | Hybrid Retrieval pipeline, reranking and evidence retrieval.                 |
| **evaluation/**   | Computes answer quality metrics such as Faithfulness and Answer Relevancy.   |
| **verification/** | Citation verification and evidence validation.                               |
| **services/**     | Connects the frontend with the backend pipeline.                             |
| **frontend/**     | Interactive Streamlit application.                                           |
| **components/**   | Modular UI components including Sidebar, Dashboard and Insights Panel.       |
| **pages/**        | Additional application pages such as Uploaded Documents and About DocuTrace. |
| **data/**         | Stores source documents and generated vector indexes.                        |


---

# 📸 User Interface

## 🏠 Dashboard

The main dashboard allows users to submit document-related queries and interact with the Agentic RAG pipeline through a modern Streamlit interface.

<p align="center">
  <img src="docs/screenshots/dashboard.png" width="900">
</p>

---

## 💡 Final Answer & Evidence

The generated answer is presented together with evidence aggregation and retrieved document sources to improve transparency and traceability.

<p align="center">
  <img src="docs/screenshots/answer.png" width="900">
</p>

---

## 📊 Insights Panel

The Insights panel provides verification status, confidence score, evaluation metrics, reflection results, and planner outputs.

<p align="center">
  <img src="docs/screenshots/insights.png" width="350">
</p>

---

## 📂 Documents

Displays information about the indexed document, embedding model, vector database, and retrieval pipeline.

<p align="center">
  <img src="docs/screenshots/documents.png" width="900">
</p>

---

## ℹ️ About DocuTrace

Summarizes the project architecture, technology stack, and system workflow.

<p align="center">
  <img src="docs/screenshots/about.png" width="900">
</p>

