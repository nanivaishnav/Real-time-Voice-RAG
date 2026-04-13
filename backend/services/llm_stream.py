from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def stream_llm(query, contexts):
    context_text = "\n".join(contexts)

    stream = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer clearly and conversationally."},
            {"role": "user", "content": f"{context_text}\n\nQuestion: {query}"}
        ],
        stream=True
    )

    async for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content