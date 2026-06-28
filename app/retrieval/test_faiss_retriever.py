from faiss_retriever import retrieve

results = retrieve(
    "How has Generative AI evolved?"
)

for i, chunk in enumerate(results):

    print(
        f"\nRESULT {i+1}\n"
    )

    print(chunk[:500])