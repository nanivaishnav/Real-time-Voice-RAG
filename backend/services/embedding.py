from fastembed import TextEmbedding

class EmbeddingService:
    def __init__(self):
        self.model = TextEmbedding()

    def embed(self, texts):
        return list(self.model.embed(texts))