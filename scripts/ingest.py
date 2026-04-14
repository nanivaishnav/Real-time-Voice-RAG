import asyncio
import os
from firecrawl import FirecrawlApp
from app.services.embedding import EmbeddingService
from app.services.qdrant_service import QdrantService
from app.utils.chunking import chunk_text

async def run():
    firecrawl = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
    embedder = EmbeddingService()

    qdrant = QdrantService(
        os.getenv("QDRANT_URL"),
        os.getenv("QDRANT_API_KEY"),
        os.getenv("COLLECTION_NAME")
    )

    res = firecrawl.crawl_url("https://docs.example.com", params={"limit": 5})

    for page in res["data"]:
        text = page.get("markdown", "")
        chunks = chunk_text(text)

        embeddings = embedder.embed(chunks)

        qdrant.upsert(embeddings, chunks, {"url": page.get("metadata", {}).get("sourceURL")})

asyncio.run(run())