import ollama
from config.config import *
from src.generation.prompt import build_prompt


def generate(query, chunks):
    prompt = build_prompt(query, chunks)
    response = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": TEMPERATURE},
    )

    return response["message"]["content"]
