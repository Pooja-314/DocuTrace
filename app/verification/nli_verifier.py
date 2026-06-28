from transformers import pipeline

# =====================================
# Load NLI Model
# =====================================

classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

# =====================================
# Example Context + Answer
# =====================================

context = """
Generative AI refers to AI systems capable
of producing text, images, music,
programming code, and other outputs.
"""

generated_answer = """
Generative AI can generate text,
images, and programming code.
"""

# =====================================
# Verification
# =====================================

candidate_labels = [
    "supported",
    "unsupported"
]

result = classifier(
    generated_answer,
    candidate_labels,
    hypothesis_template="This statement is {} by the context."
)

# =====================================
# Output
# =====================================

print("\n========== VERIFICATION RESULT ==========\n")

print(result)
