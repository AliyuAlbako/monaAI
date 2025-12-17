from fastapi import APIRouter
from ...core.summarizer import summarize_conversations

router = APIRouter()

@router.get("/summary")
def daily_summary():
    return summarize_conversations()
