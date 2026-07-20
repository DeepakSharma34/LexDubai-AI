import json
import pickle


class BM25Retriever:

    def __init__(self):

        with open(
            "data/processed/bm25.pkl",
            "rb"
        ) as f:
            self.bm25 = pickle.load(f)

        with open(
            "data/processed/articles.json",
            "r",
            encoding="utf-8"
        ) as f:
            self.articles = json.load(f)

    def search(self, query, limit=5):

        query_tokens = query.lower().split()

        scores = self.bm25.get_scores(query_tokens)

        ranked = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True
        )[:limit]

        results = []

        for idx, score in ranked:

            article = self.articles[idx]

            results.append({
                "score": float(score),
                "article": article["article"],
                "text": article["text"],
                "start_page": article["start_page"],
                "end_page": article["end_page"],
                "document": article["metadata"]["document_title"],
                "jurisdiction": article["metadata"]["jurisdiction"],
            })

        return results