# LexDubai AI

LexDubai AI is a legal chatbot powered by Retrieval-Augmented Generation (RAG) for UAE Employment Law.

## Features

- PDF-based legal knowledge
- Semantic search with Qdrant
- Gemini 2.5 Flash
- FastAPI backend
- Streamlit frontend
- Article and page citations

## Tech Stack

- Python
- FastAPI
- Streamlit
- Google Gemini
- Qdrant
- FastEmbed

## Run

### Backend

```bash
uvicorn app.main:app --reload
```

### Frontend

```bash
streamlit run streamlit_app.py
```

## API

```
POST /api/chat
```

Example:

```json
{
  "question": "What is Annual Leave?"
}
```