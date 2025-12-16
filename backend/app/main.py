# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes_generate import router as gen_router
from app.api.v1.routes_chat import router as chat_router

app = FastAPI(title="Mona AI Backend", version="1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(gen_router, prefix="/api/v1")
app.include_router(chat_router, prefix="/api/v1")

@app.get("/")
def home():
    return {"message": "Welcome to Mona AI Backend"}
