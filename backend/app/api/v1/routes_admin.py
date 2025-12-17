from fastapi import APIRouter
from ...core.kb_loader import load_kb

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/kb")
def get_business_kb():
    return load_kb()


# @router.post("/kb")
# def update_business_kb(payload: dict):
#     save_kb(payload)
#     return {"status": "success", "message": "Business knowledge updated"}
