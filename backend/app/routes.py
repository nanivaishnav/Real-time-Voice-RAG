from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.services.llm_stream import stream_llm
from app.services.tts_stream import generate_audio
from app.services.retrieval import Retriever
from app.services.qdrant_service import QdrantService
import os
import json

router = APIRouter()

qdrant = QdrantService(
    os.getenv("QDRANT_URL"),
    os.getenv("QDRANT_API_KEY"),
    os.getenv("COLLECTION_NAME")
)

retriever = Retriever(qdrant)

@router.post("/stream")
async def stream(data: dict):
    query = data["query"]

    contexts = retriever.get_context(query)

    async def event_generator():
        full_text = ""

        async for token in stream_llm(query, contexts):
            full_text += token
            yield f"data: {json.dumps({'token': token})}\n\n"

        # final audio
        audio = await generate_audio(full_text)
        yield f"data: {json.dumps({'audio': audio.hex(), 'done': True})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")