import ollama

# =====================================
# Complex Query
# =====================================

query = """
How has Generative AI evolved
and what business impacts does it create?
"""

# =====================================
# Query Decomposition Prompt
# =====================================

decomposition_prompt = f"""
You are DocuTrace, an enterprise
multi-hop retrieval planner.

TASK:
Decompose the query into short
retrieval-focused sub-questions.

STRICT RULES:
- Output ONLY questions
- One question per line
- Maximum 10 words per question
- No explanations
- No commentary
- No labels
- No bullet points

Generate ONLY 3 retrieval questions.

Focus ONLY on:
1. AI evolution
2. Business impacts

Avoid:
- ethics
- regulations
- influencers
- public perception
- future predictions


Query:
{query}
"""


# =====================================
# Generate Sub-Questions
# =====================================

response = ollama.chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": decomposition_prompt
        }
    ]
)

sub_questions = response[
    "message"
]["content"]

# =====================================
# Output
# =====================================

print(
    "\n========== SUB QUESTIONS ==========\n"
)

print(sub_questions)


sub_question_list = [

    q.strip()

    for q in sub_questions.split("\n")

    if q.strip()
]

