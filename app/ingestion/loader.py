import fitz
from pathlib import Path


class PDFLoader:

    def __init__(self, pdf_path):
        self.pdf_path = Path(pdf_path)

    def load(self):
        document = fitz.open(self.pdf_path)

        pages = []

        for page_number, page in enumerate(document):

            text = page.get_text()

            pages.append(
                {
                    "page": page_number + 1,
                    "text": text
                }
            )

        document.close()

        return pages