from src.retrieval.pipeline import retrieve
from src.generation.generator import generate


def main():
    while True:
        query = input("\nQuestion: ")
        if query.lower() == "exit":
            break

        top_chunks = retrieve(query)

        if not top_chunks:
            print("No matching chunks found.")
            continue

        print("\nRetrieved after reranking:\n")
        for i, chunk in enumerate(top_chunks, start=1):
            print(f"\nRank {i}")
            print(f"Source : {chunk['source']}")
            print(f"Chunk ID : {chunk['chunk_id']}")
            print(f"Distance : {chunk['distance']:.4f}")
            print(f"Rerank Score: {chunk['rerank_score']:.4f}")
            print(chunk["text"])
            print("-" * 80)

        answer = generate(query, top_chunks)
        print(answer)


if __name__ == "__main__":
    main()
