# backend/app/api/v1/ai_router.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.inference_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/ask")
async def ask(req: ChatRequest):
    msg = (req.message or "").strip()
    if not msg:
        raise HTTPException(status_code=400, detail="message is required")
    reply = await generate_response(msg)
    return {"reply": reply}
