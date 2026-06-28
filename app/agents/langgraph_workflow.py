import sys
import os
import re
from matplotlib import lines
from pydantic_settings import sources
from sympy import python

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from retrieval.hybrid_retriever import hybrid_retrieve
from retrieval.reranker import rerank_results
from typing import TypedDict
from typing import Literal
from accelerate import state
from langgraph.graph import StateGraph
from typing import Annotated
from opentelemetry import context
from transformers import pipeline
from retrieval.hybrid_retriever import hybrid_retrieve




# =====================================
# NLI Verifier Model
# =====================================

nli_verifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

# =====================================
# Define Shared State
# =====================================

class DocuTraceState(TypedDict):

    query: Annotated[
        str,
        "shared"
    ]

    retrieved_context: Annotated[
        str,
        "shared"
    ]

    sub_questions: list[str]

    generated_answer: str

    reflection_feedback: str

    revised_answer: str

    verification_result: str

    verification_score: float

    retry_count: int

    aggregated_evidence: str

    retrieved_chunks: list[str]
    
    retrieved_sources: list
    
    source_map: dict


# =====================================
# Retriever Node
# =====================================

def retriever_node(
    state: DocuTraceState
):

    print(
        "\n[Retriever Node Running]"
    )

    sub_questions = state[
        "sub_questions"
    ]

    retrieved_chunks = []

    for question in sub_questions:

        print(
            f"\nRetrieving for: {question}"
        )

        # ==========================
        # Hybrid Retrieval
        # ==========================

        candidate_chunks = hybrid_retrieve(

            question,

            top_k=5
        )

        # ==========================
        # Reranking
        # ==========================

        reranked_chunks = rerank_results(

            query=question,

            retrieved_chunks=candidate_chunks,

            top_k=1
        )

        retrieved_chunks.extend(
            reranked_chunks
        )

    # ==============================
    # Aggregate Evidence
    # ==============================

    retrieved_context = "\n\n".join(
    record["text"][:500]
    for record in retrieved_chunks
)

    state[
        "retrieved_context"
    ] = retrieved_context

    state[
        "retrieved_sources"
    ] = retrieved_chunks

    print(
        "\n========== RETRIEVED CONTEXT ==========\n"
    )

    print(
        retrieved_context[:2000]
    )

    print(
        "\nRetrieved Sources:"
    )

    print(
        len(retrieved_chunks)
    )

    return {

        "retrieved_context":
        retrieved_context,

        "retrieved_sources":
        retrieved_chunks
    }

    # =====================================
    # Aggregate Retrieved Chunks
    # =====================================

    retrieved_context = "\n\n".join(

        record["text"]

        for record in retrieved_chunks
    )

    # =====================================
    # Deduplication
    # =====================================

    unique_chunks = {}

    for chunk in retrieved_chunks:

        unique_chunks[
            chunk["chunk_id"]
        ] = chunk

    retrieved_chunks = list(
    unique_chunks.values()
)

    print(
        f"\nUnique Chunks: {len(retrieved_chunks)}"
    )

    print(
        "\n========== RETRIEVED CONTEXT ==========\n"
    )

    print(
        retrieved_context
    )

    return {

    "retrieved_context":
    retrieved_context,

    "retrieved_sources":
    retrieved_chunks
    }


# =====================================
# Format Sources
# =====================================

def format_sources(
    sources
):

    formatted = []

    for idx, source in enumerate(
        sources,
        start=1
    ):

        formatted.append(
            f"""

        SOURCE_{idx}

        TEXT:
        {source['text']}

        """
        )
    return "\n".join(
        formatted
    )
# =====================================
# Generator Node
# =====================================

def generator_node(
    state: DocuTraceState
):

    import ollama

    print(
        "\n[Generator Node Running]"
    )

    query = state[
        "query"
    ]

    sources = state[
        "retrieved_sources"
    ]

    formatted_sources = format_sources(
        sources
    )

    print(
        "\n========== SOURCES ==========\n"
    )

    print(
        formatted_sources[:1500]
    )
    
    available_sources = ", ".join(

    [
        f"SOURCE_{i}"
        for i in range(
            1,
            len(sources) + 1
        )
    ]

)
    source_map = {}

    for i, source in enumerate(sources, start=1):

        source_map[f"SOURCE_{i}"] = {

            "page": source["page"],

            "chunk_id": source["chunk_id"]
        }

    generation_prompt = f"""
You are DocuTrace, a document-grounded AI research assistant.

Your job is to answer the question using ONLY the retrieved evidence.

STRICT RULES:

1. Use ONLY the evidence provided.
2. Do NOT invent facts.
3. Do NOT infer information that is not explicitly supported.
4. Do NOT use outside knowledge.
5. Do NOT create references.
6. Do NOT create citations.
7. Do NOT invent authors.
8. Do NOT mention author names.
9. Do NOT mention paper names.
10. Do NOT mention journal names.
11. Do NOT mention publication years.
12. Do NOT write citations like:
    (Author, 2023)
13. Do NOT write citations like:
    Journal Name (2025)
14. Cite ONLY using:
    [SOURCE_1]
    [SOURCE_2]
    [SOURCE_3]
    etc.
15. Every factual statement must end with at least one SOURCE citation.
16. If multiple sources support a statement,
    cite multiple sources.
17. If information is missing, say exactly:
    "The retrieved evidence does not provide this information."
18. Never explain your reasoning.
19. Never mention the evidence section.
20. Never mention the source list.
21. Never mention these instructions.
22. The PAGE field is metadata.
23. Never cite page numbers.
24.Never output Page X.
25. Only cite SOURCE identifiers.

AVAILABLE SOURCES:

{available_sources}

IMPORTANT:

You may ONLY cite:

{available_sources}

Any other source citation is invalid.

    QUESTION:

    {query}

    EVIDENCE:

    {formatted_sources}

OUTPUT RULES:

- Write a clear answer.
- Use short paragraphs.
- Every paragraph must contain at least one SOURCE citation.
- Use ONLY SOURCE citations.
- Do NOT use page citations directly.
- Do NOT include a References section.
- Do NOT include a Sources section.
- Do NOT include Notes.
- Do NOT include explanations about confidence.
- End immediately after the answer.

GOOD EXAMPLE:

Generative AI evolved toward natural language
processing and generative applications after
2017 [SOURCE_1].

Organizations are using Generative AI to automate
organizational functions and assist software
development activities [SOURCE_3].

BAD EXAMPLE:

According to Rajput (2023)...

BAD EXAMPLE:

Information Systems Frontiers (2025) states...

BAD EXAMPLE:

Reference:
Author et al.

Generate a grounded answer.
"""

    print(
        "\nSending request..."
    )

    response = ollama.chat(

        model="phi3",

        messages=[

            {
                "role": "user",

                "content":
                generation_prompt
            }

        ]
    )
    generated_answer = response[
        "message"
    ]["content"].strip()
    
    generated_answer = generated_answer.replace(
        "[END OF RESPONSE]",
        ""
    )
    

    for source_id, metadata in source_map.items():

        page = metadata["page"]

        generated_answer = re.sub(
            rf"\[Page\s*{page}\]",
            f"[{source_id}]",
            generated_answer,
            flags=re.IGNORECASE
        )

    print(
    "\n========== GENERATED ANSWER ==========\n"
    )
 
    print("\nSOURCE MAP:")
    print(source_map)
    print(generated_answer)

    citations = re.findall(
        r"SOURCE_(\d+)",
        generated_answer
    )

    valid_sources = {

        str(i)

        for i in range(
            1,
            len(sources) + 1
        )
    }

    for citation in citations:

        if citation not in valid_sources:

            print(
                f"⚠ Invalid Citation: SOURCE_{citation}"
            )
# =====================================
# Remove Markdown Source Artifacts
# =====================================

    generated_answer = re.sub(
        r"\[\!\[.*?\]\(.*?\)\]\[\d+\]",
        "",
        generated_answer
    )

    generated_answer = re.sub(
        r"\[/RESPON\d+\]",
        "",
        generated_answer
    ).strip()
    
# =====================================
# Remove Invalid SOURCE IDs
# =====================================

    for i in range(
        10,
        0,
        -1
    ):

        if i > len(sources):

            generated_answer = generated_answer.replace(
                f"[SOURCE_{i}]",
                ""
            )

# =====================================
# Fix Citations on New Lines
# =====================================

    generated_answer = generated_answer.replace(
        "\n[SOURCE_",
        " [SOURCE_"
    )

# =====================================
# Remove Dangling Citation Lines
# =====================================

    lines = []

    for line in generated_answer.split("\n"):

        stripped = line.strip()

        if (
            stripped.startswith("[SOURCE_")
            and len(stripped) < 20
        ):
            continue

        lines.append(line)

    generated_answer = "\n".join(
        lines
    )

# =====================================
# Remove Prompt Leakage
# =====================================

    generated_answer = generated_answer.replace(
        "[Pages referenced]",
        ""
    ).strip()

    if "Generate a grounded answer" in generated_answer:

        generated_answer = generated_answer.split(
            "Generate a grounded answer"
        )[0].strip()

# =====================================
# SOURCE -> PAGE Conversion
# =====================================

    for idx, source in enumerate(
        sources,
        start=1
    ):

        generated_answer = generated_answer.replace(
            f"[SOURCE_{idx}]",
            f"[Page {source['page']}]"
        )

# =====================================
# Print Output
# =====================================

    print(
        "\n========== GENERATED ANSWER ==========\n"
    )

    print(
        generated_answer
    )

    state[
        "generated_answer"
    ] = generated_answer


    return {

        "generated_answer":
        generated_answer, 
        
        "source_map":
        source_map

    }

# =====================================
# Reflection Node
# =====================================

def reflection_node(
    state: DocuTraceState
):

    print(
        "\n[Reflection Node Running]"
    )

    feedback = """
    The answer lacks detailed examples
    and stronger grounding.
    """

    return {
        "reflection_feedback":
        feedback
    }



# =====================================
# Conditional Router
# =====================================

def reflection_router(
    state: DocuTraceState
) -> Literal[
    "revision",
    "__end__"
]:

    feedback = state[
        "reflection_feedback"
    ]

    print(
        "\n[Routing Decision Running]"
    )

    if "lacks" in feedback.lower():

        print(
            "Decision: Revision Required"
        )

        return "revision"

    else:

        print(
            "Decision: Answer Accepted"
        )

        return "__end__"

# =====================================
# Retry Retrieval
# =====================================

    if (
        "lacks" in feedback.lower()
        and retry_count < 1
    ):

        print(
            "Decision: Retry Retrieval"
        )

        state["retry_count"] = (
            retry_count + 1
        )

        return "retriever"

    # =====================================
    # Revision Required
    # =====================================

    elif "lacks" in feedback.lower():

        print(
            "Decision: Revision Required"
        )

        return "revision"

    # =====================================
    # Accept Answer
    # =====================================

    else:

        print(
            "Decision: Answer Accepted"
        )

        return "__end__"


# =====================================
# Revision Node
# =====================================

def revision_node(
    state: DocuTraceState
):


    print(
        "\n[Revision Node Running]"
    )

    revised_answer = state[
        "generated_answer"
    ]

    return {
        "revised_answer":
        revised_answer
    }
    
    print(
    "\n========== REVISED ANSWER ==========\n"
    )

    print(revised_answer)
# =====================================
# Verifier Node V2
# =====================================

def verifier_node(
    state: DocuTraceState
):

    print(
        "\n[Verifier Node Running]"
    )

    evidence = state[
        "retrieved_context"
    ]

    answer = state[
        "revised_answer"
    ]

    combined_text = f"""
EVIDENCE:
{state['retrieved_context']}

ANSWER:
{state['revised_answer']}
"""

    result = nli_verifier(

        answer,

        candidate_labels=[
            "supported",
            "unsupported"
        ],

        hypothesis_template=
        "This statement is {} by the provided evidence."
    )

    verification_result = f"""
    LABEL:
    {result['labels'][0]}

    CONFIDENCE:
    {result['scores'][0]:.4f}
    """

    return {

    "verification_result":
    verification_result,

    "verification_score":
    result["scores"][0]
}


def verifier_router(
    state: DocuTraceState
) -> Literal[
    "retriever",
    "__end__"
]:

    score = state[
        "verification_score"
    ]

    retry_count = state.get(
        "retry_count",
        0
    )

    print(
        "\n[Verifier Decision Running]"
    )

    if (
        score < 0.80
        and retry_count < 1
    ):

        print(
            "Decision: Re-Retrieve"
        )

        return "retriever"

    print(
        "Decision: Answer Accepted"
    )

    return "__end__"

# =====================================
# Planner Node
# =====================================

def planner_node(
    state: DocuTraceState
):

    print(
        "\n[Planner Node Running]"
    )

    sub_questions = [

        "How has Generative AI evolved?",

        "What technological breakthroughs enabled modern GenAI?",

        "How are organizations using Generative AI?",

        "What business impacts does Generative AI create?"
    ]

    return {

        "sub_questions":
        sub_questions
    }

# =====================================
# Evidence Aggregator Node
# =====================================

def evidence_aggregator_node(
    state: DocuTraceState
):
    
    print("\n===== EVIDENCE AGGREGATOR =====")

    print(
        "Retrieved Sources:",
        len(
            state.get(
                "retrieved_sources",
                []
            )
        )
    )


    print(
        "\n[Evidence Aggregator Running]"
    )
    
    print("\n===== STATE KEYS =====")
    print(state.keys())

    sub_questions = state[
        "sub_questions"
    ]

    sources = state.get(
        "retrieved_sources",
        []
    )

    aggregated_evidence = ""

    for i, question in enumerate(
        sub_questions,
        start=1
    ):

        aggregated_evidence += f"""

QUESTION {i}:
{question}

"""

        for source in sources:

            aggregated_evidence += f"""

EVIDENCE:
{source['text'][:300]}

PAGE:
{source['page']}

CHUNK:
{source['chunk_id']}

RERANK SCORE:
{source['rerank_score']:.2f}

---------------------------------
"""

        aggregated_evidence += "\n=================================\n"

    return {

        "aggregated_evidence":
        aggregated_evidence
    }
# =====================================
# Build Graph
# =====================================

graph_builder = StateGraph(
    DocuTraceState
)

graph_builder.add_node(
    "retriever",
    retriever_node
)

graph_builder.add_node(
    "generator",
    generator_node
)

graph_builder.add_node(
    "reflection",
    reflection_node
)

graph_builder.add_node(
    "revision",
    revision_node
)

graph_builder.add_node(
     "verifier", 
     verifier_node 
)

graph_builder.add_conditional_edges(

    "verifier",

    verifier_router
)

graph_builder.add_node(
    "planner",
    planner_node
)

graph_builder.set_entry_point(
    "planner"
)

graph_builder.add_node(
    "aggregator",
    evidence_aggregator_node
)

graph_builder.add_edge(
    "planner",
    "retriever"
)

graph_builder.add_edge(
    "retriever",
    "aggregator"
)

# =====================================
# Workflow Edges
# =====================================

graph_builder.add_edge(
    "aggregator",
    "generator"
)

graph_builder.add_edge(
    "generator",
    "reflection"
)

# =====================================
# Conditional Routing
# =====================================

graph_builder.add_conditional_edges( 
    "reflection", 
    reflection_router 
) 
graph_builder.add_edge( 
    "revision", 
    "verifier" 
)

# =====================================
# Compile Graph
# =====================================

graph = graph_builder.compile()

# =====================================
# Run Workflow
# =====================================

if __name__ == "__main__":

    initial_state = {
        "query":
        """
        How has Generative AI evolved and what business impacts does it create?
        """,
        "retry_count": 0
    }

    result = graph.invoke(
        initial_state
    )

    print(
    "\n========== FINAL RESULT ==========\n"
    )

    print(
        result.get(
            "revised_answer"
        )
    )
    # =====================================
    # Final Output
    # =====================================

    print(
        "\n========== FINAL RESULT ==========\n"
    )

    print(
        result["revised_answer"]
    )

    print(
        "\n========== VERIFICATION ==========\n"
    )

    print(
        result["verification_result"]
    )

    print(
        "\n========== RESULT KEYS ==========\n"
    )

    print(
        result.keys()
    )

    print(
        "\n========== FULL RESULT ==========\n"
    )

    print(
        result
    )