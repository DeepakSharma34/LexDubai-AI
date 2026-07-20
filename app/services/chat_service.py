from app.retrieval.retriever import LegalRetriever
from app.llm.gemini_client import GeminiClient
from app.config.prompt import build_prompt


class ChatService:

    def __init__(self):
        self.retriever = LegalRetriever()
        self.llm = GeminiClient()

    def ask(self, question: str):

        documents = self.retriever.search(question)

        if not documents:
            return {
                "answer": "I couldn't find any relevant information in the UAE Employment Law.",
                "sources": []
            }

        prompt = build_prompt(question, documents)

        answer = self.llm.generate(prompt)

        sources = []

        for doc in documents:
            sources.append({
                "article": doc["article"],
                "page": f"{doc['start_page']}-{doc['end_page']}"
            })

        return {
            "answer": answer,
            "sources": sources
        }