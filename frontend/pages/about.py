import streamlit as st

def render_about():
    st.title("ℹ️ About DocuTrace")

    st.markdown("""
    ## Multi-Hop Document Intelligence with Verifiable Citation Chains

    DocuTrace is an enterprise-inspired Agentic Retrieval-Augmented Generation (RAG) system designed to answer questions from documents while providing transparent evidence, citation verification, and evaluation metrics.

    Unlike traditional document chatbots, DocuTrace decomposes complex queries into sub-questions, retrieves the most relevant evidence, generates grounded responses, and evaluates the quality of each answer.

    ---
    """)

    st.subheader("🏗️ System Architecture")

    st.code("""
    📄 PDF Documents
            │
            ▼
    Text Extraction & Chunking
            │
            ▼
    Sentence Embeddings
            │
            ▼
    FAISS Vector Store
            │
            ▼
    Hybrid Retrieval
            │
            ▼
    Planner Agent
            │
            ▼
    Generator Agent
            │
            ▼
    Reflection Agent
            │
            ▼
    Verification & Evaluation
    """)
    st.subheader("🚀 Key Features")

    st.markdown("""
    - Multi-Agent LangGraph Workflow
    - Hybrid Retrieval (Dense + BM25)
    - Semantic Document Retrieval
    - FAISS Vector Database
    - Local LLM (Phi-3 via Ollama)
    - Evidence Aggregation
    - Citation-aware Responses
    - Reflection-based Answer Refinement
    - Faithfulness Evaluation
    - Context Precision & Recall Metrics
    - Interactive Streamlit Dashboard
    """)
    
    st.subheader("🛠️ Technology Stack")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
    **Backend**
    Python
    LangGraph
    LangChain
    Ollama
    Phi-3
    FAISS
    Sentence Transformers
    """)

    with col2:
        st.markdown("""
    **Frontend**
    Streamlit
    Custom CSS
    PyMuPDF
    Scikit-learn
    NumPy
    """)

    st.divider()

    st.caption("""
    Developed by Pooja Singh

    AI Engineer & Generative AI Portfolio Project

    © 2026 DocuTrace
    """)    