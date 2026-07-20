from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from fastembed import TextEmbedding

from app.config.settings import (
    QDRANT_PATH,
    COLLECTION_NAME,
)


class VectorStore:

    def __init__(self):

        self.client = QdrantClient(path=QDRANT_PATH)

        self.embedding_model = TextEmbedding(
        model_name="BAAI/bge-base-en-v1.5"
)

        collections = self.client.get_collections().collections

        names = [c.name for c in collections]

        if COLLECTION_NAME not in names:

            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE
                )
            )

    def embed(self, text):

        return list(self.embedding_model.embed([text]))[0].tolist()