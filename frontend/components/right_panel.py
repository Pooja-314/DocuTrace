import streamlit as st


def render_right_panel(result):

    st.subheader("Insights")

    # =====================================
    # Verification
    # =====================================

    st.markdown("### Verification")

    if result["verification"]["label"] == "SUPPORTED":

        st.success(
            result["verification"]["label"]
        )

    else:

        st.error(
            result["verification"]["label"]
        )

    st.metric(
        "Confidence",
        f"{result['verification']['confidence']:.1%}"
    )

    st.metric(
        "Sources Retrieved",
        len(result.get("sources", []))
    )

    st.metric(
        "Sub Questions",
        len(
            result["reasoning"].get(
                "sub_questions",
                []
            )
        )
    )

    st.divider()

    # =====================================
    # Evaluation
    # =====================================

    st.subheader("Evaluation")

    evaluation = result["evaluation"]

    st.success(
        f"Faithfulness: {evaluation['faithfulness']['label']}"
    )

    st.caption(
        f"Confidence: {evaluation['faithfulness']['confidence']:.0%}"
    )

    st.success(
        f"Answer Relevancy: {evaluation['answer_relevancy']['label']}"
    )

    st.caption(
        f"Confidence: {evaluation['answer_relevancy']['confidence']:.0%}"
    )

    st.metric(
        "Context Precision",
        f"{evaluation['context_precision']['precision']:.2f}"
    )

    st.metric(
        "Context Recall",
        f"{evaluation['context_recall']['recall']:.2f}"
    )

    st.divider()

    # =====================================
    # Reflection
    # =====================================

    st.markdown("### Reflection")

    st.success("Reflection Completed")

    st.divider()

    # =====================================
    # Agent Reasoning
    # =====================================

    st.subheader("Agent Reasoning")

    with st.expander("🧠 Planner"):

        sub_questions = result["reasoning"].get(
            "sub_questions",
            []
        )

        if sub_questions:

            for question in sub_questions:

                st.write(f"• {question}")

        else:

            st.info(
                "No sub-questions generated."
            )

    with st.expander("🔍 Reflection"):

        st.write(

            result["reasoning"].get(

                "reflection",

                "No reflection feedback available."

            )

        )