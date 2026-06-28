import ollama

# =====================================
# Original Query
# =====================================

query = """
How has Generative AI evolved
and what business impacts does it create?
"""

# =====================================
# Generated Answer
# =====================================

generated_answer = """
Generative AI evolved from symbolic AI
toward deep learning and transformer-based
large language models.

It impacts businesses through automation,
decision support, software development,
and content generation.
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
# Reflection Prompt
# =====================================

reflection_prompt = f"""
You are DocuTrace, an enterprise
AI reflection agent.

Your task is to critically evaluate
the generated answer using the
retrieved evidence.

Check for:
1. Hallucinations
2. Missing information
3. Weak reasoning
4. Unsupported claims
5. Citation grounding quality

Return:
- Overall assessment
- Problems found
- Suggested improvements

QUERY:
{query}

GENERATED ANSWER:
{generated_answer}

RETRIEVED EVIDENCE:
{aggregated_evidence}
"""

# =====================================
# Run Reflection Agent
# =====================================

print(
    "\nRunning reflection analysis..."
)

response = ollama.chat(

    model="phi3",

    messages=[
        {
            "role": "user",

            "content": reflection_prompt
        }
    ]
)

reflection_output = response[
    "message"
]["content"]

# =====================================
# Output
# =====================================

print(
    "\n========== REFLECTION OUTPUT ==========\n"
)

print(reflection_output)

