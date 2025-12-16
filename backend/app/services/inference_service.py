# backend/app/services/inference_service.py
import asyncio
from datetime import datetime
from app.core.model_loader import load_model
from app.core.config import settings
import logging

LOG = logging.getLogger("monaai.infer")
LOG.setLevel(logging.INFO)

# Lazy load model on first request (or call load_model() at startup)
_model, _tokenizer, _device = None, None, None

def _ensure_loaded():
    global _model, _tokenizer, _device
    if _model is None or _tokenizer is None:
        _model, _tokenizer, _device = load_model()
    return _model, _tokenizer, _device

async def generate_response(user_message: str) -> str:
    model, tokenizer, device = _ensure_loaded()

    # Build chat-style prompt
    messages = [
        {"role": "system", "content": "You are Mona AI, a friendly multilingual assistant."},
        {"role": "user", "content": user_message}
    ]
    date_str = datetime.now().strftime("%d %b %Y")
    prompt = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=False,
        date_string=date_str
    )

    inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
    if device == "cuda":
        inputs = {k: v.to("cuda") for k, v in inputs.items()}

    # Blocking model.generate; run in executor so event loop isn't blocked
    loop = asyncio.get_running_loop()

    def _gen():
        out = model.generate(
            **inputs,
            max_new_tokens=settings.MAX_NEW_TOKENS,
            temperature=settings.TEMPERATURE,
            repetition_penalty=settings.REPETITION_PENALTY,
            do_sample=False
        )
        return out

    try:
        outputs = await loop.run_in_executor(None, _gen)
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # strip assistant header if present
        if "assistant" in decoded:
            decoded = decoded.split("assistant")[-1].strip()
        return decoded
    except Exception as e:
        LOG.exception("Generation failed: %s", e)
        return "Sorry, I couldn't generate a response right now."
