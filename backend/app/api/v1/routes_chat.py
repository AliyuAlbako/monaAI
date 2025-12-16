from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ...core.model_loader import load_model
import traceback

router = APIRouter(prefix="/chat", tags=["Customer Chat"])

SYSTEM_PROMPT = (
    "You are Mona AI, a friendly Nigerian business assistant. "
    "Reply naturally to the user in the SAME language they used "
    "(English, Pidgin, Hausa, Yoruba, or Igbo). "
    "Do not repeat instructions. "
    "Do not simulate the user."
)

@router.post("")
def chat(message: str)->JSONResponse:
    try:
        llm = load_model()

        prompt = (
            f"<s>[INST] <<SYS>> {SYSTEM_PROMPT} <</SYS>> "
            f"{message.strip()} [/INST]"
        )

        output = llm(
            prompt,
            max_tokens=150,
            temperature=0.6,
            top_p=0.9,
            repeat_penalty=1.1,
            stop=["</s>", "[INST]"]
        )

        text = output["choices"][0]["text"].strip()

        return {"response": text}

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})
