import google.generativeai as genai

from app.config.settings import (
    GOOGLE_API_KEY,
    LLM_MODEL,
)


genai.configure(api_key=GOOGLE_API_KEY)


class GeminiClient:

    def __init__(self):
        self.model = genai.GenerativeModel(LLM_MODEL)

    def generate(self, prompt: str) -> str:

        response = self.model.generate_content(prompt)

        return response.text.strip()