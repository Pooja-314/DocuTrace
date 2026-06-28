from transformers import pipeline

# =====================================
# Zero-Shot Intent Classifier
# =====================================

classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

# =====================================
# Example Queries
# =====================================

queries = [

    "What is Generative AI?",

    "How does GenAI compare to traditional AI?",

    "Why do large language models hallucinate?",

    "How has AI evolved since 2020?"
]

candidate_labels = [ "fact lookup question", 
                    "comparison question", 
                    "cause and effect question", 
                    "time-based evolution question" 
                    ]
# =====================================
# Classification
# =====================================

print("\n========== QUERY INTENTS ==========\n")

for query in queries:

    result = classifier(
        query,
        candidate_labels
    )

    predicted_intent = result["labels"][0] 
    predicted_intent = predicted_intent.replace( 
        " question", 
        "" 
        )

    confidence = result["scores"][0]

    print(f"\nQuery: {query}")

    print(f"Intent: {predicted_intent}")

    print(f"Confidence: {confidence:.4f}")

