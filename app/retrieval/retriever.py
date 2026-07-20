from app.config.settings import COLLECTION_NAME
from app.retrieval.vector_store import VectorStore
from app.retrieval.bm25_retriever import BM25Retriever
from app.retrieval.fusion import reciprocal_rank_fusion


class LegalRetriever:

    def __init__(self):

        self.vector_store = VectorStore()
        self.bm25 = BM25Retriever()

    def vector_search(self, query, limit=5):

        embedding = self.vector_store.embed(query)

        results = self.vector_store.client.query_points(
            collection_name=COLLECTION_NAME,
            query=embedding,
            limit=limit,
        )

        documents = []

        for point in results.points:

            payload = point.payload

            documents.append({
                "score": round(point.score, 4),
                "article": payload["article"],
                "text": payload["text"],
                "start_page": payload["start_page"],
                "end_page": payload["end_page"],
                "document": payload["document"],
                "jurisdiction": payload["jurisdiction"],
            })

        return documents

    def search(self, query, limit=5):

        vector_results = self.vector_search(
            query=query,
            limit=limit
        )

        bm25_results = self.bm25.search(
            query=query,
            limit=limit
        )

        final_results = reciprocal_rank_fusion(
            vector_results,
            bm25_results
        )

        return final_results[:limit]