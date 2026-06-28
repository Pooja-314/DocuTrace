import streamlit as st


def render_sidebar():

    st.markdown("## 📄 DocuTrace")

    st.divider()

    page = st.radio(
        "",
        [
            "🏠 Dashboard",
            "📂 Uploaded Documents",
            "ℹ️ About DocuTrace"
        ]
    )

    st.divider()

    st.markdown("### System Status")

    st.markdown(
        """
        <div class="status-card">

        🟢 <b>Phi-3</b> Online<br><br>

        🟢 <b>FAISS</b> Ready<br><br>

        🟢 <b>LangGraph</b> Active<br><br>

        🟢 <b>Hybrid Retrieval</b> Enabled

        </div>
        """,
        unsafe_allow_html=True
    )

    return page