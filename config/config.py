# Chunking Configuration
from pathlib import Path

# Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "data" / "dataset"
CHROMA_DIR = BASE_DIR / "data" / "chroma_db"

# ChromaDB
COLLECTION_NAME = "wikipedia"

# Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 2

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Retrieval
DENSE_TOP_K = 15

# Reranker
RERANK_TOP_K = 4
RERANK_MODEL = "BAAI/bge-reranker-base"

# Generation
LLM_MODEL = "llama3.2:latest"
TEMPERATURE = 0.1

# Evaluation
DENSE_DISTANCE_THRESHOLD = 999
RERANKED_SCORE_THRESHOLD = -999