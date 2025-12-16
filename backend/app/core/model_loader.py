# from llama_cpp import Llama
# from pathlib import Path
# import os
#
# print("🧠 model_loader.py FILE:", __file__)
# print("📂 Current working directory:", os.getcwd())
#
# BASE_DIR = Path(__file__).resolve().parent.parent
# MODEL_PATH = BASE_DIR / "models" / "N-ATLaS-GGUF-Q4_K_M.gguf"
#
# print("📍 BASE_DIR:", BASE_DIR)
# print("📍 MODEL_PATH:", MODEL_PATH)
# print("📦 Model exists?", MODEL_PATH.exists())
#
# _cached_model = None
#
# def load_model():
#     global _cached_model
#
#     if _cached_model is None:
#         if not MODEL_PATH.exists():
#             raise FileNotFoundError(f"❌ Model not found at: {MODEL_PATH}")
#
#         print("🔄 Loading Mona AI GGUF model...")
#
#         _cached_model = Llama(
#             model_path=str(MODEL_PATH),
#             n_ctx=2048,
#             n_threads=8,
#             verbose=True
#         )
#
#         print("✅ Model loaded")
#
#     return _cached_model

# backend/app/core/model_loader.py
from pathlib import Path
from llama_cpp import Llama


#  versio 2
# BASE_DIR = Path(__file__).resolve().parent.parent
# MODEL_PATH = BASE_DIR / "models" / "N-ATLaS-GGUF-Q4_K_M.gguf"
#
# _cached_model = None
#
# def load_model():
#     global _cached_model
#     if _cached_model is None:
#         if not MODEL_PATH.exists():
#             raise FileNotFoundError(f"Model not found: {MODEL_PATH}")
#         _cached_model = Llama(model_path=str(MODEL_PATH))
#     return _cached_model

from llama_cpp import Llama
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "N-ATLaS-GGUF-Q4_K_M.gguf")

_llm = None

def load_model():
    global _llm
    if _llm is None:
        print("🔄 Loading N-ATLaS GGUF model...")
        _llm = Llama(
            model_path=MODEL_PATH,
            n_ctx=2048,
            n_threads=4,
            n_batch=128,
            verbose=False
        )
        print("✅ Model loaded successfully")
    return _llm

