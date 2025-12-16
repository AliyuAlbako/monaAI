# from fastapi import APIRouter
# from fastapi.responses import JSONResponse
# from ...core.model_loader import load_model
# import traceback
#
# router = APIRouter()
#
# @router.post("/generate")
# def generate_text(prompt: str):
#     try:
#         llm = load_model()
#
#         SYSTEM_PROMPT = (
#             "You are Mona AI, a Nigerian business assistant. "
#             "Reply directly to the user. Do NOT repeat system instructions. "
#             "Answer in the most appropriate Nigerian language."
#         )
#
#         full_prompt = f"""<s>[INST] <<SYS>>
# {SYSTEM_PROMPT}
# <</SYS>>
#
# {prompt}
# [/INST]"""
#
#         result = llm(
#             full_prompt,
#             max_tokens=200,
#             temperature=0.7,
#             top_p=0.9,
#             repeat_penalty=1.1,
#             stop=["</s>"]
#         )
#
#         text = result["choices"][0]["text"].strip()
#
#         return {"response": text}
#
#     except Exception as e:
#         traceback.print_exc()
#         return JSONResponse(
#             status_code=500,
#             content={"error": str(e)}
#         )

# backend/app/api/v1/routes_generate.py

# 2nd
# from fastapi import APIRouter
# from fastapi.responses import JSONResponse
# from ...core.model_loader import load_model
# import traceback
#
# router = APIRouter()
#
# @router.post("/generate")
# def generate_text(prompt: str):
#     try:
#         model = load_model()
#
#         SYSTEM_PROMPT = (
#             "You are Mona AI, a friendly Nigerian business assistant. "
#             "You respond helpfully in Nigerian languages such as English, Pidgin, "
#             "Hausa, Yoruba, and Igbo. Always give your best possible answer."
#         )
#         formatted_prompt = f"<s>[INST] <<SYS>> {SYSTEM_PROMPT} <</SYS>> {prompt} [/INST]"
#
#         output = model(formatted_prompt, max_tokens=200, temperature=0.8, top_p=0.9)
#         text = output['choices'][0]['text']
#
#         return {"response": text}
#
#     except Exception as e:
#         print("\n----- ERROR IN /generate -----")
#         traceback.print_exc()
#         print("--------------------------------\n")
#         return JSONResponse(status_code=500, content={"error": str(e)})
#
# @router.get("/health")
# def health_check():
#     return {"status": "ok", "message": "Backend running"}
# 3rd


# backend/app/api/v1/routes_generate.py
# backend/app/api/v1/routes_generate.py
# 4th


# backend/app/api/v1/routes_generate.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ...core.model_loader import load_model
import traceback
import re

router = APIRouter()

SYSTEM_PROMPT = (
    "You are Mona AI, a Nigerian business assistant. "
    "Reply directly to the user in the SAME language as the input "
    "(English, Pidgin, Hausa, Yoruba, Igbo). "
    "Do not repeat instructions. "
    "Do not include system messages. "
    "Answer naturally and politely."
)

def clean_output(text: str) -> str:
    """
    Remove any leaked instruction tokens or system prompts
    """
    text = re.sub(r"\[INST\].*?\[/INST\]", "", text, flags=re.DOTALL)
    text = re.sub(r"<<SYS>>.*?<</SYS>>", "", text, flags=re.DOTALL)
    text = text.replace("<s>", "").replace("</s>", "")
    return text.strip()

@router.post("/generate")
def generate_text(prompt: str):
    try:
        llm = load_model()

        final_prompt = (
            f"<s>[INST] <<SYS>> {SYSTEM_PROMPT} <</SYS>> {prompt.strip()} [/INST]"
        )

        output = llm(
            final_prompt,
            max_tokens=200,
            temperature=0.6,
            top_p=0.9,
            repeat_penalty=1.15,
            stop=["[INST]", "</s>", "<s>"]  # 🔑 THIS IS CRITICAL
        )

        raw_text = output["choices"][0]["text"]
        text = clean_output(raw_text)

        if not text:
            text = "Sorry, I didn’t catch that. Please try again."

        return {"response": text}

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})


@router.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend running"}

