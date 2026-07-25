from config.config import *
from src.embeddings.embedding import encode_documents
from src.ingestion.clean import load_documents
from src.ingestion.chunking import chunk_text
from src.ingestion.vector_store import get_collection, store_embeddings

def run_ingestion(pdf_folder=DATASET_DIR):
    # Extract text from PDFs
    documents = load_documents(pdf_folder)

    # Chunk documents
    chunks = []
    for doc in documents:
        doc_chunks = chunk_text(
            doc["text"],
            doc["source"],
            chunk_size=CHUNK_SIZE,
            overlap_sent=CHUNK_OVERLAP,
        )
        chunks.extend(doc_chunks)

    # Generate embeddings
    chunk_texts = [chunk["text"] for chunk in chunks]
    embeddings = encode_documents(chunk_texts)

    collection = get_collection()
    store_embeddings(collection, chunks, embeddings)

    return chunks
