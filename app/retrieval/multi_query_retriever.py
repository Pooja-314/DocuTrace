# =====================================
# Original Query
# =====================================

query = "What is Generative AI?"

# =====================================
# Multi-Query Expansion
# =====================================

expanded_queries = [

    query
]

if "Generative AI" in query:

    expanded_queries.extend([

        "What are large language models?",

        "How does GenAI generate content?",

        "What is AI-generated text?",

        "How do generative models work?"
    ])



# =====================================
# Simulated Retrieval Strategies
# =====================================

print("\n========== MULTI-QUERY RETRIEVAL ==========\n")

for i, expanded_query in enumerate(expanded_queries):

    print(f"\n--- QUERY {i+1} ---")

    print(expanded_query)

    print(
        "\n[Simulated Retrieval]"
    )

    print(
        "Searching vector index..."
    )

    print(
        "Searching BM25..."
    )

    print(
        "Applying reranking..."
    )

