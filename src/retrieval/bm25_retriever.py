from nltk.tokenize import word_tokenize
from rank_bm25 import BM25Okapi


def bm25_score(query, chunks):
    tokenized_docs = [word_tokenize(chunk["text"].lower()) for chunk in chunks]
    bm25 = BM25Okapi(tokenized_docs)

    tokenized_query = word_tokenize(query.lower())
    scores = bm25.get_scores(tokenized_query)

    for chunk, score in zip(chunks, scores):
        chunk["bm25_score"] = float(score)

    return chunks
