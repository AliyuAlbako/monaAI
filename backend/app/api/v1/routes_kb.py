from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json
import os

router = APIRouter(prefix="/kb", tags=["Knowledge Base"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
KB_PATH = os.path.join(BASE_DIR, "data", "business_kb.json")

@router.post("/upload")
def upload_kb(payload: dict):
    try:
        with open(KB_PATH, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)

        return {"status": "success", "message": "Knowledge base updated"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@router.get("/view")
def view_kb():
    if not os.path.exists(KB_PATH):
        return {}

    with open(KB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json
import os

router = APIRouter(prefix="/kb", tags=["Knowledge Base"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
KB_PATH = os.path.join(BASE_DIR, "data", "business_kb.json")

@router.post("/upload")
def upload_kb(payload: dict):
    try:
        with open(KB_PATH, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)

        return {"status": "success", "message": "Knowledge base updated"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@router.get("/view")
def view_kb():
    if not os.path.exists(KB_PATH):
        return {}

    with open(KB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
