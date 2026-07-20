from pathlib import Path


class MetadataExtractor:

    @staticmethod
    def extract(pdf_path):

        file = Path(pdf_path)

        return {

            "document_title": file.stem,

            "jurisdiction": "UAE",

            "authority": "Official Government Source",

            "source_url": "",

            "effective_date": "",

            "document_version": ""
        }