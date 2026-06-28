from transformers import pipeline

# =====================================
# Query Intent Classifier
# =====================================

classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

candidate_labels = [
    "fact lookup",
    "comparison",
    "cause and effect",
    "time-based evolution"
]

# =====================================
# Example Queries
# =====================================

queries = [

    "What is Generative AI?",

    "How does GenAI compare to traditional AI?",

    "Why do LLMs hallucinate?",

    "How has AI evolved since 2020?"
]

# =====================================
# Retrieval Strategy Router
# =====================================

def adaptive_retrieval(intent):

    if intent == "fact lookup":

        return {
            "top_k": 2,
            "retrieval_mode": "precise"
        }

    elif intent == "comparison":

        return {
            "top_k": 5,
            "retrieval_mode": "broad_context"
        }

    elif intent == "cause and effect":

        return {
            "top_k": 4,
            "retrieval_mode": "reasoning_focused"
        }

    elif intent == "time-based evolution":

        return {
            "top_k": 6,
            "retrieval_mode": "metadata_aware"
        }

    else:

        return {
            "top_k": 3,
            "retrieval_mode": "default"
        }


# =====================================
# Run Classification + Routing
# =====================================

print("\n========== ADAPTIVE RETRIEVAL ==========\n")

for query in queries:

    result = classifier(
        query,
        candidate_labels
    )

    predicted_intent = result["labels"][0]

    confidence = result["scores"][0]

    strategy = adaptive_retrieval(
        predicted_intent
    )

    print(f"\nQuery: {query}")

    print(f"Intent: {predicted_intent}")

    print(f"Confidence: {confidence:.4f}")

    print("Routing Strategy:", strategy)


