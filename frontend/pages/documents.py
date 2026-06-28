import streamlit as st


def render_documents():

    st.title("📂 Uploaded Documents")

    st.markdown(
        """
        View information about the document currently indexed by DocuTrace.
        """
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Pages",
            23
        )

        st.metric(
            "Chunks",
            153
        )

        st.metric(
            "Embedding Model",
            "BAAI/bge-small"
        )

    with col2:

        st.metric(
            "Vector Store",
            "FAISS"
        )

        st.metric(
            "Retriever",
            "Hybrid"
        )

        st.metric(
            "LLM",
            "Phi-3"
        )

    st.divider()

    st.subheader("📄 Indexed Document")

    st.info(
        "Generative_Artificial_Intelligence_Evolving_Techno.pdf"
    )

    st.caption(
        "Status: Indexed ✓ | Ready for Retrieval"
    )