import ollama

from app.agents.langgraph_workflow import DocuTraceState

# =====================================
# User Query
# =====================================

query = """
How has Generative AI evolved
and what business impacts
does it create?
"""

# =====================================
# Planner Prompt
# =====================================

planner_prompt = f"""
You are DocuTrace Planner Agent.

Your task is to break a complex query
into smaller retrieval questions.

Rules:
- Generate 3 to 5 sub-questions
- Keep them concise
- Ensure they help answer
  the original query

QUERY:
{query}
"""

def planner_node(
    state: DocuTraceState
):

    query = state["query"]

    if query.lower().startswith("what is"):

        return {
            "sub_questions": [query]
        }

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": planner_prompt.format(
                    query=query
                )
            }
        ]
    )

    plan = response["message"]["content"]

    print(
        "\n========== QUERY PLAN ==========\n"
    )

    print(plan)

    # ==========================
    # Parse Plan
    # ==========================

    sub_questions = [

        line.strip("-•123456789. ")

        for line in plan.split("\n")

        if line.strip()
    ]

    return {

        "sub_questions":
        sub_questions
    }