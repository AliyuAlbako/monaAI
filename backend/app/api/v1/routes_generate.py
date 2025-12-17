# from fastapi import APIRouter
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
# import uuid
# import traceback
#
# from ...core.model_loader import load_model
# from ...core.kb_loader import load_kb
# from ...core.lang_detect import detect_language
# from ...core.memory_store import save_message
#
# router = APIRouter()
#
# # ✅ Load model ONCE
# llm = load_model()
#
# # ======================
# # SYSTEM PROMPT
# # ======================
# SYSTEM_PROMPT = (
#     "You are Mona AI, a helpful Nigerian business assistant.\n"
#     "Rules:\n"
#     "- If the user greets, reply with a polite greeting only.\n"
#     "- Do NOT introduce business details unless asked.\n"
#     "- If the question is about the business, use the provided business information.\n"
#     "- Reply directly and clearly.\n"
#     "- Respond in the SAME language as the user.\n\n"
# )
#
# # ======================
# # LANGUAGE CONTROL
# # ======================
# LANG_PROMPTS = {
#     "ha": "Answer in Hausa only.",
#     "yo": "Dahun ni Yoruba nikan.",
#     "ig": "Zaa azịza n'asụsụ Igbo naanị.",
#     "pidgin": "Reply for Pidgin English.",
#     "en": "Answer in English."
# }
#
# # ======================
# # REQUEST SCHEMA
# # ======================
# class GenerateRequest(BaseModel):
#     prompt: str
#     session_id: str | None = None
#
#
# # ======================
# # GREETING DETECTOR
# # ======================
# def is_greeting(text: str) -> bool:
#     greetings = [
#         "hello", "hi", "hey",
#         "ina kwana", "ya kake", "yaya kake",
#         "bawo", "eku ile", "e kaaro",
#         "kedu", "ututu oma",
#         "how far"
#     ]
#     text = text.lower()
#     return any(greet in text for greet in greetings)
#
#
# # ======================
# # MAIN GENERATE ROUTE
# # ======================
# @router.post("/generate")
# def generate_text(payload: GenerateRequest):
#     try:
#         prompt = payload.prompt.strip()
#         if not prompt:
#             return {"response": "Don Allah, ka saka tambaya mai ma'ana."}
#
#         session_id = payload.session_id or str(uuid.uuid4())
#         user_lang = detect_language(prompt)
#         lang_instruction = LANG_PROMPTS.get(user_lang, LANG_PROMPTS["en"])
#         user_text = prompt.lower()
#
#         save_message(session_id, "user", prompt)
#
#         # ======================
#         # GREETING SHORT-CIRCUIT
#         # ======================
#         if is_greeting(prompt):
#             greetings_reply = {
#                 "ha": "Lafiya lau, na gode. Yaya zan taimaka?",
#                 "yo": "Mo wa daadaa. Bawo ni mo ṣe le ran ọ lọwọ?",
#                 "ig": "Adị m mma. Kedu ka m ga-esi nyere gị?",
#                 "pidgin": "I dey well. How I fit help you?",
#                 "en": "I’m fine, thank you. How can I help you?"
#             }
#             return {
#                 "session_id": session_id,
#                 "response": greetings_reply.get(user_lang, greetings_reply["en"])
#             }
#
#         # ======================
#         # LOAD BUSINESS KB
#         # ======================
#         kb = load_kb()
#
#         # ======================
#         # FAQ MATCHING (FAST)
#         # ======================
#         if kb and "faqs" in kb:
#             for faq in kb["faqs"]:
#                 if faq["q"].lower() in user_text:
#                     return {
#                         "session_id": session_id,
#                         "response": faq["a"]
#                     }
#
#         # ======================
#         # PRICE LIST MATCHING
#         # ======================
#         if kb and "price_list" in kb:
#             for item in kb["price_list"]:
#                 if item["item"].lower() in user_text:
#                     return {
#                         "session_id": session_id,
#                         "response": f"{item['item']} na {item['price']}."
#                     }
#
#         # ======================
#         # QUICK BUSINESS INFO
#         # ======================
#         if kb:
#             if "location" in user_text:
#                 return {
#                     "session_id": session_id,
#                     "response": f"Muna nan a {kb.get('location')}."
#                 }
#
#             if "delivery" in user_text:
#                 return {
#                     "session_id": session_id,
#                     "response": kb.get("delivery")
#                 }
#
#             if "open" in user_text or "working" in user_text or "hours" in user_text:
#                 return {
#                     "session_id": session_id,
#                     "response": kb.get("working_hours")
#                 }
#
#         # ======================
#         # FALLBACK → MODEL
#         # ======================
#         business_context = ""
#         if kb:
#             business_context = (
#                 f"Business Name: {kb.get('business_name','')}\n"
#                 f"Description: {kb.get('description','')}\n"
#                 f"Location: {kb.get('location','')}\n"
#                 f"Working Hours: {kb.get('working_hours','')}\n"
#                 f"Delivery: {kb.get('delivery','')}\n"
#             )
#
#         final_prompt = (
#             SYSTEM_PROMPT +
#             f"Language Rule: {lang_instruction}\n\n"
#             "Business Information:\n" +
#             business_context +
#             "\nCustomer Question:\n" +
#             prompt +
#             "\nAnswer:\n"
#         )
#
#         output = llm(
#             final_prompt,
#             max_tokens=150,
#             temperature=0.6,
#             top_p=0.9,
#             repeat_penalty=1.1,
#             stop=["Customer Question:", "Answer:"]
#         )
#
#         text = output["choices"][0]["text"].strip()
#         if not text:
#             text = "Don Allah, ka sake tambaya."
#
#         save_message(session_id, "assistant", text)
#
#         return {
#             "session_id": session_id,
#             "response": text,
#             "language": user_lang
#         }
#
#     except Exception as e:
#         traceback.print_exc()
#         return JSONResponse(status_code=500, content={"error": str(e)})
#
#
# # ======================
# # HEALTH CHECK
# # ======================
# @router.get("/health")
# def health_check():
#     return {"status": "ok", "message": "Backend running"}


# # ==================Last

from fastapi import APIRouter
from pydantic import BaseModel
from ...core.model_loader import load_model
from ...core.kb_loader import load_kb
from ...core.lang_detect import detect_language
from ...core.memory_store import save_message
import uuid

router = APIRouter()

llm = load_model()
kb = load_kb()
# =========================
# SYSTEM PROMPT
# =========================
SYSTEM_PROMPT = (
    "You are Mona AI, a Nigerian business assistant.\n"
    "Rules:\n"
    "- If the user greets you, respond with a greeting ONLY.\n"
    "- Do NOT invent information.\n"
    "- Use provided business information when relevant.\n"
    "- Respond in the SAME language as the user.\n"
    "- Be polite, clear, and brief.\n\n"
)

# =========================
# REQUEST MODEL
# =========================
class GenerateRequest(BaseModel):
    prompt: str
    session_id: str | None = None


# =========================
# GREETING DETECTOR
# =========================
def is_greeting(text: str) -> bool:
    greetings = [
        "hello", "hi", "hey",
        "ina kwana", "ya kake", "yaya kake",
        "eku ile", "e kaaro",
        "kedu", "ututu oma",
        "how far"
    ]
    text = text.lower()
    return any(g in text for g in greetings)


# =========================
# GREETING REPLIES
# =========================
GREETINGS_REPLY = {
    "ha": "Lafiya lau, na gode. Yaya zan taimaka?",
    "yo": "Mo wa daadaa. Bawo ni mo ṣe le ran ọ lọwọ?",
    "ig": "Adị m mma. Kedu ka m ga-esi nyere gị?",
    "pidgin": "I dey well. How I fit help you?",
    "en": "I’m fine, thank you. How can I help you?"
}


# =========================
# MAIN ROUTE
# =========================
@router.post("/generate")
def generate_text(payload: GenerateRequest):
    prompt = payload.prompt.strip()
    session_id = payload.session_id or str(uuid.uuid4())
    lang = detect_language(prompt)

    if not prompt:
        return {"response": "Don Allah, ka rubuta tambaya mai ma'ana."}

    save_message(session_id, "user", prompt)

    # =========================
    # GREETING SHORT-CIRCUIT
    # =========================
    if is_greeting(prompt):
        reply = GREETINGS_REPLY.get(lang, GREETINGS_REPLY["en"])
        save_message(session_id, "assistant", reply)
        return {"session_id": session_id, "response": reply}

    user_text = prompt.lower()

    # =========================
    # FAQ MATCH (SAFE)
    # =========================
    faqs_block = kb.get("faqs")
    if isinstance(faqs_block, dict):
        for faq in faqs_block.get("faqs", []):
            if any(k in user_text for k in faq.get("keywords", [])):
                return {
                    "session_id": session_id,
                    "response": faq.get("answer")
                }

    # =========================
    # MENU / PRICE MATCH (SAFE)
    # =========================
    menu_block = kb.get("menu")
    if isinstance(menu_block, dict):
        for item in menu_block.get("menu", []):
            if any(k in user_text for k in item.get("keywords", [])):
                return {
                    "session_id": session_id,
                    "response": f"{item.get('item')} na ₦{item.get('price')}."
                }

    # =========================
    # LOCATION (SAFE)
    # =========================
    delivery = kb.get("delivery")
    if isinstance(delivery, dict):
        location = delivery.get("location")
        if location and any(k in user_text for k in ["where", "location", "address"]):
            return {
                "session_id": session_id,
                "response": f"Muna nan a {location.get('area')}, {location.get('city')}."
            }

    # =========================
    # WORKING HOURS (SAFE)
    # =========================
    hours = kb.get("hours")
    if isinstance(hours, dict):
        wh = hours.get("working_hours")
        if wh and any(k in user_text for k in ["open", "time", "hour"]):
            return {
                "session_id": session_id,
                "response": f"Muna bude daga {wh.get('open_time')} zuwa {wh.get('close_time')}."
            }

    # =========================
    # FALLBACK TO MODEL (SAFE)
    # =========================
    profile = kb.get("profile", {})
    business_context = (
        f"Business: {kb['profile']['business_name']}\n"
        f"Description: {kb['profile']['description']}\n"
        f"Location: {kb['delivery']['location']['area']}, {kb['delivery']['location']['city']}\n"
    )

    final_prompt = (
        SYSTEM_PROMPT +
        business_context +
        f"User Question:\n{prompt}\nAnswer:"
    )

    output = llm(
        final_prompt,
        max_tokens=100,
        temperature=0.5,
        top_p=0.9,
        repeat_penalty=1.1,
        stop=["\n\n", "</s>"]
        # stop=["User Question:", "Answer:"]

    )

    text = output["choices"][0]["text"].strip()

    if not text:
        text = GREETINGS_REPLY.get(lang, GREETINGS_REPLY["en"])

    save_message(session_id, "assistant", text)

    return {"session_id": session_id, "response": text}


@router.get("/health")
def health_check():
    return {"status": "ok"}


