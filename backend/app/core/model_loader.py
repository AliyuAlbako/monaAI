from llama_cpp import Llama
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "N-ATLaS-GGUF-Q4_K_M.gguf"

_cached_model = None

def load_model():
    global _cached_model

    if _cached_model is None:
        print(f"🔄 Loading model from: {MODEL_PATH}")

        if not MODEL_PATH.exists():
            raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

        _cached_model = Llama(
            model_path=str(MODEL_PATH),
            n_ctx=4096,
            n_threads=8,
            n_batch=512,
            verbose=False,
            use_mmap = True,
            use_mlock = False
        )

        print("✅ Mona AI model loaded successfully")

    return _cached_model
