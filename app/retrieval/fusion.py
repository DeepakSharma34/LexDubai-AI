def reciprocal_rank_fusion(vector_results, bm25_results, k=60):

    scores = {}

    documents = {}

    for rank, doc in enumerate(vector_results):

        key = doc["article"]

        scores[key] = scores.get(key, 0) + 1 / (k + rank)

        documents[key] = doc

    for rank, doc in enumerate(bm25_results):

        key = doc["article"]

        scores[key] = scores.get(key, 0) + 1 / (k + rank)

        documents[key] = doc

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        documents[key]
        for key, _ in ranked
    ]