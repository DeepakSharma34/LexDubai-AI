import json

from app.ingestion.loader import PDFLoader
from app.ingestion.cleaner import TextCleaner
from app.ingestion.metadata import MetadataExtractor
from app.ingestion.chunker import LegalArticleChunker


PDF_PATH = "data/raw/uae_employment_law.pdf"


def main():

    print("Loading PDF...")

    loader = PDFLoader(PDF_PATH)
    pages = loader.load()

    print(f"Loaded {len(pages)} pages")

    print("Cleaning pages...")

    clean_pages = []

    for page in pages:

        clean_pages.append(
            {
                "page": page["page"],
                "text": TextCleaner.clean(page["text"])
            }
        )

    metadata = MetadataExtractor.extract(PDF_PATH)

    print("Chunking articles...")

    chunker = LegalArticleChunker()

    chunks = chunker.chunk(clean_pages)

    output = []

    for chunk in chunks:

        output.append(
            {
                **chunk,
                "metadata": metadata
            }
        )

    with open(
        "data/processed/articles.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(output, f, indent=4, ensure_ascii=False)

    print(f"Created {len(output)} article chunks")


if __name__ == "__main__":
    main()