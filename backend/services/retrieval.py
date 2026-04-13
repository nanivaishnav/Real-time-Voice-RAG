from app.services.embedding import EmbeddingService

class Retriever:
    def __init__(self, qdrant):
        self.qdrant = qdrant
        self.embedder = EmbeddingService()

    def get_context(self, query):
        vec = self.embedder.embed([query])[0]
        results = self.qdrant.search(vec.tolist())

        return [r.payload["content"] for r in results.points]