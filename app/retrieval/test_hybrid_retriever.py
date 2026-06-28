from hybrid_retriever import hybrid_retrieve

results = hybrid_retrieve(
    "How has Generative AI evolved?"
)

print(results[0])

for i, chunk in enumerate(results):

    print(
        f"\n========== RESULT {i+1} ==========\n"
    )

    print(
        f"Page: {chunk['page']}"
    )

    print(
        f"Chunk ID: {chunk['chunk_id']}"
    )

    print(
        chunk["text"][:500]
    )