from sentence_transformers import CrossEncoder
from config.config import *

reranker = CrossEncoder(RERANK_MODEL)

def rerank(query, chunks):
    pairs = [[query, chunk["text"]] for chunk in chunks]
    scores = reranker.predict(pairs)

    for chunk, score in zip(chunks, scores):
        chunk["rerank_score"] = float(score)

    chunks.sort(key=lambda x: x["rerank_score"], reverse=True)
    return chunks


def rerank_filter(chunks):
    filtered = [chunk for chunk in chunks if chunk["rerank_score"] >= RERANKED_SCORE_THRESHOLD]
    return filtered[:RERANK_TOP_K]
