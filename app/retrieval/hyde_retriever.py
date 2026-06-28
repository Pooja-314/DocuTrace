import ollama

# =====================================
# User Query
# =====================================

query = "What is Generative AI?"

# =====================================
# HyDE Prompt
# =====================================

hyde_prompt = f"""
You are DocuTrace, an enterprise AI system.

Generate a concise, factual hypothetical
document passage that could answer the
following question.

Do not mention that this is hypothetical.

Question:
{query}
"""

# =====================================
# Generate Hypothetical Document
# =====================================

print(
    "\nGenerating hypothetical answer "
    "for retrieval augmentation..."
)

response = ollama.chat(

    model="phi3",

    messages=[
        {
            "role": "user",

            "content": hyde_prompt
        }
    ]
)

# =====================================
# Extract Generated Content
# =====================================

hypothetical_document = response[
    "message"
]["content"]

# =====================================
# Output
# =====================================

print(
    "\n========== HYDE DOCUMENT ==========\n"
)

print(hypothetical_document)

print(
    "\n========== HYDE STATUS ==========\n"
)

print(
    "Hypothetical document generated "
    "successfully."
)

