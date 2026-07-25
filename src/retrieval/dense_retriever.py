import chromadb
from config.config import *
from src.embeddings.embedding import encode_query

client = chromadb.PersistentClient(path=str(CHROMA_DIR))
collection = client.get_collection(COLLECTION_NAME)


def dense_retrieve(query, top_k=DENSE_TOP_K):
    query_embedding = encode_query(query)
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)

    chunks = []
    for i in range(len(results["ids"][0])):
        chunks.append(
            {
                "text": results["documents"][0][i],
                "source": results["metadatas"][0][i]["source"],
                "chunk_id": results["metadatas"][0][i]["chunk_id"],
                "distance": results["distances"][0][i],
            }
        )
    return chunks
