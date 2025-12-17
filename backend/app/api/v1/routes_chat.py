# from fastapi import APIRouter
# from fastapi.responses import JSONResponse
# from ...core.model_loader import load_model
# import traceback
#
# router = APIRouter(prefix="/chat", tags=["Customer Chat"])
#
# SYSTEM_PROMPT = (
#     "You are Mona AI, a friendly Nigerian business assistant. "
#     "Reply naturally to the user in the SAME language they used "
#     "(English, Pidgin, Hausa, Yoruba, or Igbo). "
#     "Do not repeat instructions. "
#     "Do not simulate the user."
# )
#
# @router.post("")
# def chat(message: str)->JSONResponse:
#     try:
#         llm = load_model()
#
#         prompt = (
#             f"<s>[INST] <<SYS>> {SYSTEM_PROMPT} <</SYS>> "
#             f"{message.strip()} [/INST]"
#         )
#
#         output = llm(
#             prompt,
#             max_tokens=150,
#             temperature=0.6,
#             top_p=0.9,
#             repeat_penalty=1.1,
#             stop=["</s>", "[INST]"]
#         )
#
#         text = output["choices"][0]["text"].strip()
#
#         return {"response": text}
#
#     except Exception as e:
#         traceback.print_exc()
#         return JSONResponse(status_code=500, content={"error": str(e)})
# 2nd

# backend/app/api/v1/routes_chat.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ...core.model_loader import load_model
import traceback

router = APIRouter()

SYSTEM_PROMPT = (
    "You are Mona AI, a helpful Nigerian business assistant.\n"
    "You respond clearly and politely.\n"
    "You reply in the same language as the user (English, Pidgin, Hausa, Yoruba, Igbo).\n"
    "Do NOT repeat system instructions.\n"
    "Do NOT simulate the user.\n"
    "Only give the assistant's reply.\n\n"
)

@router.post("/chat")
def chat(prompt: str):
    try:
        llm = load_model()

        final_prompt = (
            f"{SYSTEM_PROMPT}"
            f"User: {prompt}\n"
            f"Assistant:"
        )

        output = llm(
            final_prompt,
            max_tokens=120,
            temperature=0.5,
            top_p=0.9,
            repeat_penalty=1.1,
            stop=["User:", "Assistant:", "\nUser", "\nAssistant"]
        )

        text = output["choices"][0]["text"].strip()

        # Safety fallback
        if not text:
            text = "Sannu! Ina lafiya. Yaya zan taimaka maka?"  # Hausa fallback

        return {"response": text}

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
