from src.retrieval.hybrid_retriever import hybrid_retrieve, similarity_filter
from src.reranking.reranker import rerank, rerank_filter


def retrieve(query):
    chunks = hybrid_retrieve(query)
    chunks = similarity_filter(chunks)
    chunks = rerank(query, chunks)
    chunks = rerank_filter(chunks)
    return chunks
