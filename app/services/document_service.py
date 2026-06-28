# app/services/document_service.py

import re
from app.agents.langgraph_workflow import graph
from app.evaluation.evaluation_runner import run_evaluation


def build_verification(result):

    score = result.get(
        "verification_score",
        0
    )

    return {
        "label":
        "SUPPORTED" if score >= 0.5
        else "UNSUPPORTED",

        "confidence":
        round(score, 3)
    }

def replace_source_citations(
    answer,
    sources
):

    for i, source in enumerate(
        sources,
        start=1
    ):

        answer = answer.replace(

            f"[SOURCE_{i}]",

            f"[Page {source['page']}]"
        )

    return answer

    
def answer_question(query: str):

    initial_state = {
        "query": query
    }
    
    result = graph.invoke(initial_state)

    answer = replace_source_citations(

        result.get(
            "revised_answer",
            ""
        ),

        result.get(
            "retrieved_sources",
            []
        )
    )

    evaluation = run_evaluation(
        question=query,
        retrieved_context=result.get(
            "retrieved_context",
            ""
        ),
        generated_answer=result.get(
            "revised_answer",
            ""
        )
    )

    print("\n=== EVALUATION ===\n")
    print(evaluation)

    return {

        "query":
        result.get("query"),

        "answer":
        answer,

        "sources":
        result.get("retrieved_sources", []),
        
        "source_map":
        result.get("source_map", {}),

        "verification":
        build_verification(result),

        "evaluation":
        evaluation,

        "reasoning": {

            "sub_questions":
            result.get("sub_questions"),

            "reflection":
            result.get("reflection_feedback")
        },

        "evidence":
        result.get("aggregated_evidence")
    }