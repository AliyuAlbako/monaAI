# backend/app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # load from .env if exists

class Settings:
    NATLAS_LOCAL_PATH: str = os.getenv("NATLAS_LOCAL_PATH", "./N-ATLaS")
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    MAX_NEW_TOKENS: int = int(os.getenv("MAX_NEW_TOKENS", "200"))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.2"))
    REPETITION_PENALTY: float = float(os.getenv("REPETITION_PENALTY", "1.08"))

settings = Settings()
