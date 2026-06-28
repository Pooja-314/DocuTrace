import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import streamlit as st

from styles import CUSTOM_CSS

from components.sidebar import render_sidebar
from components.dashboard import render_dashboard
from components.right_panel import render_right_panel

from pages.documents import render_documents
from pages.about import render_about

st.set_page_config(
    page_title="DocuTrace",
    page_icon="📄",
    layout="wide"
)

st.markdown(
    CUSTOM_CSS,
    unsafe_allow_html=True
)

left, center, right = st.columns([1,3,1])

# ------------------------
# Sidebar
# ------------------------

with left:
    page = render_sidebar()

# ------------------------
# Center
# ------------------------

with center:

    if page == "🏠 Dashboard":
        render_dashboard()

    elif page == "📂 Uploaded Documents":
        render_documents()

    elif page == "ℹ️ About DocuTrace":
        render_about()

# ------------------------
# Right Panel
# ------------------------

with right:

    if "result" in st.session_state:

        render_right_panel(
            st.session_state["result"]
        )

    else:

        st.subheader("Insights")

        st.info(
            "Run a query to view insights."
        )