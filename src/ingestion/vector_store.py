import chromadb
from config.config import CHROMA_DIR, COLLECTION_NAME

def get_collection(path=CHROMA_DIR, name=COLLECTION_NAME, reset=True):
    client = chromadb.PersistentClient(path=path)

    if reset:
        try:
            client.delete_collection(name)
        except Exception:
            pass

    collection = client.get_or_create_collection(
        name=name,
        metadata={"hnsw:space": "cosine"},
    )
    return collection


def store_embeddings(collection, chunks, embeddings):
    chunk_texts = [chunk["text"] for chunk in chunks]

    collection.add(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        embeddings=embeddings.tolist(),
        documents=chunk_texts,
        metadatas=[
            {
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
            }
            for chunk in chunks
        ],
    )
