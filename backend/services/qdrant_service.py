from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
from qdrant_client.http import models
import uuid

class QdrantService:
    def __init__(self, url, api_key, collection):
        self.client = QdrantClient(url=url, api_key=api_key)
        self.collection = collection

    def create(self, dim):
        try:
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE)
            )
        except:
            pass

    def upsert(self, embeddings, chunks, metadata):
        points = [
            models.PointStruct(
                id=str(uuid.uuid4()),
                vector=emb.tolist(),
                payload={"content": chunk, **metadata}
            )
            for chunk, emb in zip(chunks, embeddings)
        ]

        self.client.upsert(self.collection, points)

    def search(self, vector, limit=5):
        return self.client.query_points(
            collection_name=self.collection,
            query=vector,
            limit=limit,
            with_payload=True
        )