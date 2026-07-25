from config.config import *
from src.retrieval.dense_retriever import dense_retrieve
from src.retrieval.bm25_retriever import bm25_score


def hybrid_retrieve(query):
    dense_chunks = dense_retrieve(query)
    dense_chunks = bm25_score(query, dense_chunks)
    return dense_chunks


def similarity_filter(chunks):
    filtered = []
    for chunk in chunks:
        if chunk["distance"] <= DENSE_DISTANCE_THRESHOLD:
            filtered.append(chunk)
    return filtered
