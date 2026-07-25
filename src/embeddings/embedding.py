from sentence_transformers import SentenceTransformer
from config.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def encode_documents(chunk_texts):
    embeddings = model.encode(
        chunk_texts,
        batch_size=32,
        normalize_embeddings=True,
    )
    return embeddings

def encode_query(query):
    query_embedding = model.encode(query, normalize_embeddings=True).tolist()
    return query_embedding