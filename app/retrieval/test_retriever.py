from app.retrieval.retriever import LegalRetriever


def main():

    retriever = LegalRetriever()

    query = "What is the probation period?"

    results = retriever.search(query)

    print("\nTop Results\n")

    for i, result in enumerate(results, start=1):

        print("=" * 70)
        print(f"Rank: {i}")
        print(f"Score: {result['score']}")
        print(f"Article: {result['article']}")
        print(f"Pages: {result['start_page']} - {result['end_page']}")
        print(f"Document: {result['document']}")
        print()
        print(result["text"][:400])
        print()


if __name__ == "__main__":
    main()