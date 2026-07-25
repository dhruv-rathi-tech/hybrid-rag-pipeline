NO_CONTEXT_MESSAGE = "I don't have enough information in the provided documents."


def build_prompt(query, chunks):
    context = ""
    for i, chunk in enumerate(chunks, start=1):
        context += f"""
Source: {chunk['source']}
Chunk: {chunk['chunk_id']}
{chunk['text']}

"""
    prompt = f"""
You are a helpful AI assistant.
Answer the user's question ONLY using the information provided in the context.
If the answer is not present in the context, reply exactly: "{NO_CONTEXT_MESSAGE}"
If multiple context sections contribute to the answer, combine them naturally.
Always cite the source after every statement.

Context: {context}
Question: {query}
Answer:
"""

    return prompt