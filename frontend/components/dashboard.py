import streamlit as st    
import re
from app.services.document_service import answer_question


def render_dashboard():

    st.markdown("""
        <div class='glow'>
        DOCUTRACE
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <center>

        Multi-Hop Document Intelligence
        with Verifiable Citation Chains

        </center>

        <div class="hero-card">

        <h3>🚀 Agentic RAG Engine</h3>

        ✅ Multi-Hop Reasoning • ✅ Citation Verification

        ✅ Evidence Aggregation • ✅ Reflection Agent

        ✅ Faithfulness Evaluation • ✅ Hybrid Retrieval

        </div>

        """,
        unsafe_allow_html=True
    )

    query = st.text_area(

        "Ask a question",

        placeholder="Example: What are the major applications of Generative AI discussed in this document?",

        height=150
    )

    if st.button("🚀 Ask DocuTrace", use_container_width=True):

        if not query.strip():

            st.warning("Please enter a question.")

            return

        with st.spinner(...):

            result = answer_question(query)

        st.session_state["result"] = result


    # ===========================================
    # Display Results
    # ===========================================

    if "result" in st.session_state:

        result = st.session_state["result"]

        # ==========================
        # Answer
        # ==========================

        st.markdown(
            '<div class="glass-card">',
            unsafe_allow_html=True
        )

        st.subheader("💡 Final Answer")

        answer = result["answer"]

        matches = re.findall(
            r"\[SOURCE_(\d+)\]",
            answer
        )

        for match in matches:

            source_num = int(match)

            answer = answer.replace(
                f"[SOURCE_{source_num}]",
                f"📄 Source {source_num}"
            )

        st.markdown(answer)

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        # ==========================
        # Evidence Aggregation
        # ==========================

        st.subheader("📚 Evidence Aggregation")

        with st.expander("📋 View Aggregated Evidence"):

            st.write(result["evidence"])

        # ==========================
        # Retrieved Sources
        # ==========================

        st.divider()

        st.subheader("📄 Retrieved Sources")

        for i, source in enumerate(result["sources"], start=1):

            with st.expander(
                f"📄 Page {source['page']} | Source {i}"
            ):

                st.code(source["chunk_id"])

                st.write(source["text"])
                
        st.divider()

        st.markdown(
            """
        <div style="text-align:center;color:gray;font-size:13px">

        © 2026 DocuTrace

        Multi-Hop Document Intelligence with Verifiable Citation Chains

        Powered by LangGraph • Phi-3 • FAISS • Streamlit

        </div>
        """,
            unsafe_allow_html=True
        )
                            
