from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: list


@router.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        response = chat_service.ask(request.question)

        return ChatResponse(
            answer=response["answer"],
            sources=response["sources"],
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )