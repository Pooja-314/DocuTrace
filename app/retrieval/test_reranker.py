from reranker import rerank_results

retrieved_chunks = [

    {
        "text":
        "Generative AI evolved from symbolic AI to deep learning.",

        "page": 1,

        "chunk_id": "chunk_1"
    },

    {
        "text":
        "Cats are popular household pets.",

        "page": 2,

        "chunk_id": "chunk_2"
    },

    {
        "text":
        "Transformer models enabled modern Generative AI systems.",

        "page": 3,

        "chunk_id": "chunk_3"
    }
]

results = rerank_results(

    query="How has Generative AI evolved?",

    retrieved_chunks=retrieved_chunks,

    top_k=2
)

for i, record in enumerate(results):

    print(
        f"\nRESULT {i+1}\n"
    )

    print(
        f"Page: {record['page']}"
    )

    print(
        f"Chunk ID: {record['chunk_id']}"
    )

    print(
        f"Score: {record['rerank_score']}"
    )

    print(
        record["text"]
    )

