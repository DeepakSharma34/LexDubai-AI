import json
import pickle

from rank_bm25 import BM25Okapi
from qdrant_client.models import PointStruct

from app.retrieval.vector_store import VectorStore
from app.config.settings import COLLECTION_NAME


def main():

    store = VectorStore()

    print("Loading articles...")

    with open(
        "data/processed/articles.json",
        "r",
        encoding="utf-8"
    ) as f:
        articles = json.load(f)

 

    tokenized_docs = [
        article["text"].lower().split()
        for article in articles
    ]

    bm25 = BM25Okapi(tokenized_docs)

    with open(
        "data/processed/bm25.pkl",
        "wb"
    ) as f:
        pickle.dump(bm25, f)

    print("BM25 index created.")

   

    points = []

    for idx, article in enumerate(articles):

        embedding = store.embed(article["text"])

        payload = {
            "article": article["article"],
            "text": article["text"],
            "start_page": article["start_page"],
            "end_page": article["end_page"],
            "document": article["metadata"]["document_title"],
            "jurisdiction": article["metadata"]["jurisdiction"],
        }

        points.append(
            PointStruct(
                id=idx,
                vector=embedding,
                payload=payload,
            )
        )

    print("Uploading vectors...")

    store.client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )

    print(f"Indexed {len(points)} articles.")

    store.client.close()


if __name__ == "__main__":
    main()