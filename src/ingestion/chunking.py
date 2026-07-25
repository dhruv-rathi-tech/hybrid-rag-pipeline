from nltk.tokenize import sent_tokenize
from config.config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_text(text, source, chunk_size=CHUNK_SIZE, overlap_sent=CHUNK_OVERLAP):
    sentences = sent_tokenize(text)
    chunks = []
    current_sentences = []
    current_chunk = ""
    chunk_id = 0

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_sentences.append(sentence)
            current_chunk += sentence + " "
        else:
            chunks.append(
                {
                    "text": current_chunk.strip(),
                    "source": source,
                    "chunk_id": chunk_id,
                }
            )
            chunk_id += 1
            current_sentences = current_sentences[-overlap_sent:]
            current_chunk = " ".join(current_sentences)
            if current_chunk:
                current_chunk += " "
            current_sentences.append(sentence)
            current_chunk += sentence + " "

    if current_chunk:
        chunks.append(
            {
                "text": current_chunk.strip(),
                "source": source,
                "chunk_id": chunk_id,
            }
        )

    return chunks
