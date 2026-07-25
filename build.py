from src.ingestion.ingest import run_ingestion
from config.config import DATASET_DIR


def main():
    chunks = run_ingestion(pdf_folder=DATASET_DIR)

if __name__ == "__main__":
    main()
