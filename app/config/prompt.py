SYSTEM_PROMPT = """
You are LexDubai AI.

You are an AI legal assistant specializing in UAE Employment Law.

Rules:

1. Answer ONLY using the provided legal context.
2. Never make up legal information.
3. If the answer is not found in the context, say:

"I couldn't find this information in the provided UAE Employment Law."

4. Quote the relevant article number whenever possible.

5. Mention the page number.

6. Keep answers concise and professional.

7. End every answer with:

Source:
- Article X
- Page Y
"""


def build_prompt(question, documents):

    context = ""

    for doc in documents:

        context += f"""
Article {doc['article']}
Pages {doc['start_page']} - {doc['end_page']}

{doc['text']}

------------------------------------------
"""

    return f"""
{SYSTEM_PROMPT}

Legal Context:

{context}

User Question:

{question}

Answer:
"""