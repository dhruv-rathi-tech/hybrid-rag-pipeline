import os
import re
import fitz
from config.config import DATASET_DIR

def clean_text(text):
    text = text.replace("-\n", "")
    text = text.replace("\n", "\n")
    text = re.sub(r"\[\d+\]", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def load_documents(pdf_folder=DATASET_DIR):
    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

    documents = []
    for file in pdf_files:
        pdf = fitz.open(os.path.join(pdf_folder, file))
        text = ""
        for page in pdf:
            text += clean_text(page.get_text()) + "\n"
        documents.append(
            {
                "source": file,
                "text": text,
            }
        )

    return documents