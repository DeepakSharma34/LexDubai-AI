import re


class LegalArticleChunker:

    ARTICLE_PATTERN = re.compile(
    r"Article\s*[()]*\s*(\d+)\s*[()]*",
    flags=re.IGNORECASE,
)

    def chunk(self, pages):

        chunks = []

        current_article = None
        current_text = []
        start_page = None

        for page in pages:

            page_number = page["page"]
            text = page["text"]

            matches = list(self.ARTICLE_PATTERN.finditer(text))

            if not matches:

                if current_article is not None:
                    current_text.append(text)

                continue

            split_positions = [m.start() for m in matches]
            split_positions.append(len(text))

            for i, match in enumerate(matches):

                article_number = match.group(1)

                start = split_positions[i]
                end = split_positions[i + 1]

                article_text = text[start:end].strip()

                if current_article is not None:

                    chunks.append(
                        {
                            "article": current_article,
                            "text": "\n".join(current_text),
                            "start_page": start_page,
                            "end_page": page_number,
                        }
                    )

                current_article = article_number
                current_text = [article_text]
                start_page = page_number

        if current_article is not None:

            chunks.append(
                {
                    "article": current_article,
                    "text": "\n".join(current_text),
                    "start_page": start_page,
                    "end_page": pages[-1]["page"],
                }
            )

        return chunks