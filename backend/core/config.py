import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # 🔑 API KEYS
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    QDRANT_URL: str = os.getenv("QDRANT_URL")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY")
    FIRECRAWL_API_KEY: str = os.getenv("FIRECRAWL_API_KEY")

    # 🧠 VECTOR DB
    COLLECTION_NAME: str = os.getenv("COLLECTION_NAME", "docs_embeddings")

    # ⚡ PERFORMANCE
    TOP_K: int = int(os.getenv("TOP_K", 5))
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 500))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 50))

    # 🎙️ VOICE
    DEFAULT_VOICE: str = os.getenv("DEFAULT_VOICE", "coral")

    # 🚀 SERVER
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))


settings = Settings()