# Hybrid RAG System

A local Hybrid Retrieval-Augmented Generation pipeline combining dense (embedding) search,
BM25 lexical search, and cross-encoder reranking, backed by a local LLM via Ollama.

## Project Structure

```
.
├── config/
│   └── config.py               # All tunable parameters
├── data/
│   └── dataset/                 # Place source PDFs here for ingestion
├── src/
│   ├── embeddings/
│   │   └── embedding.py           # Shared SentenceTransformer wrapper 
│   ├── ingestion/
│   │   ├── clean.py               # PDF text extraction + cleaning (PyMuPDF)
│   │   ├── chunking.py            # Sentence-aware recursive chunking
│   │   ├── vector_store.py        # ChromaDB collection creation + storage
│   │   └── ingest.py              # Orchestrates: load -> chunk -> embed -> store
│   ├── retrieval/
│   │   ├── dense_retriever.py     # ChromaDB similarity search
│   │   ├── bm25_retriever.py      # BM25 lexical scoring
│   │   ├── hybrid_retriever.py    # Combines dense + BM25, applies similarity threshold
│   │   └── pipeline.py            # Top-level retrieve() — full retrieval + rerank pipeline
│   ├── reranking/
│   │   └── reranker.py             # Cross-encoder scoring + top-k filtering
│   ├── evaluation/
│   │   └── llm_evaluation.py         # LLM-based yes/no gate: "can this context answer the query?"
│   └── generation/
│       ├── prompts.py                # Prompt templates (answer prompt + evaluation prompt)
│       └── generator.py               # generate() — orchestrates can_answer() + LLM call
├── build.py                     # Entry point: runs all pre-retrieval work (ingestion/indexing)
├── main.py                      # Entry point: retrieval -> reranking -> evaluation -> generation
└── requirements.txt
```

## How It Works

1. **`build.py`** — pre-retrieval work. Calls `src/ingestion/ingest.py`, which loads PDFs from
   `data/dataset/` (`clean.py`), chunks them (`chunking.py`), embeds them
   (`src/embeddings/embedding.py`), and stores them in a persistent ChromaDB collection
   (`vector_store.py`).

2. **`main.py`** — everything from retrieval to generation. For each query:
   - `src/retrieval/pipeline.py` runs dense search (`dense_retriever.py`) + BM25
     (`bm25_retriever.py`), combined and filtered in `hybrid_retriever.py`.
   - Results are reranked with a cross-encoder (`src/reranking/reranker.py`) and cut to top-k.
   - `src/evaluation/answerability.py` gates whether the retrieved context can actually answer
     the question before generation is attempted.
   - `src/generation/generator.py` builds the final grounded prompt (`prompts.py`) and calls the
     local LLM via Ollama.

## Setup

```bash
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt')"
```

Make sure [Ollama](https://ollama.com) is installed and running locally with the model
specified in `config/config.py` (`LLM_MODEL = "llama3.2"`):

```bash
ollama pull llama3.2
```

## Usage

**1. Add your PDFs** to `data/dataset/`.

**2. Build the index:**

```bash
python build.py
```

**3. Run the QA loop:**

```bash
python main.py
```

Type your question at the prompt, or type `exit` to quit.

## Notes

- All configuration lives in `config/config.py` — nothing else hardcodes chunk sizes, top-k
  values, thresholds, or model names.
- `src/embeddings/embedder.py` is shared between ingestion and retrieval so the embedding model
  is loaded once and reused rather than duplicated.
- Each pipeline stage (ingestion, retrieval, reranking, evaluation, generation) is independently
  testable and swappable.
