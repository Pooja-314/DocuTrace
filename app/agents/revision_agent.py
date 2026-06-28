import ollama

# =====================================
# Original Query
# =====================================

query = """
How has Generative AI evolved
and what business impacts does it create?
"""

# =====================================
# Initial Generated Answer
# =====================================

initial_answer = """
Generative AI evolved from symbolic AI
toward deep learning and transformer-based
large language models.

It impacts businesses through automation,
decision support, software development,
and content generation.
"""

# =====================================
# Reflection Feedback
# =====================================

reflection_feedback = """
The answer lacks detailed historical
milestones and specific business examples.

Citation grounding is weak because
page references are missing.

More specificity about deep learning,
transformers, and enterprise adoption
would improve answer quality.
"""

# =====================================
# Aggregated Evidence
# =====================================

aggregated_evidence = """
PAGE: 3
AI evolved from symbolic approaches
toward deep learning and large-scale
neural networks.

PAGE: 15
Generative AI impacts business through
automation, decision support,
content generation, and software
development acceleration.
"""

# =====================================
# Revision Prompt
# =====================================

revision_prompt = f"""
You are DocuTrace, an enterprise
AI revision agent.

Your task is to improve the answer
using:
1. Reflection feedback
2. Retrieved evidence

STRICT RULES:
- Keep answer factual
- Avoid hallucinations
- Use only provided evidence
- Improve specificity
- Add citation grounding

STRICT RULES: 
- Do NOT invent references 
- Do NOT invent citations 
- Do NOT create fake sources 
- Use ONLY provided evidence 
- Cite ONLY provided PAGE numbers

QUERY:
{query}

INITIAL ANSWER:
{initial_answer}

REFLECTION FEEDBACK:
{reflection_feedback}

RETRIEVED EVIDENCE:
{aggregated_evidence}
"""

# =====================================
# Run Revision Agent
# =====================================

print(
    "\nRunning revision agent..."
)

response = ollama.chat(

    model="phi3",

    messages=[
        {
            "role": "user",

            "content": revision_prompt
        }
    ]
)

revised_answer = response[
    "message"
]["content"]

# =====================================
# Output
# =====================================

print(
    "\n========== REVISED ANSWER ==========\n"
)

print(revised_answer)

