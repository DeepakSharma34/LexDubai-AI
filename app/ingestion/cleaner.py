import re


class TextCleaner:

    @staticmethod
    def clean(text):

        text = re.sub(r"\n+", "\n", text)

        text = re.sub(r"[ \t]+", " ", text)

        text = re.sub(r"\s{2,}", " ", text)

        return text.strip()