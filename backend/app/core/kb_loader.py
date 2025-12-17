#
# import os
#
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# KB_PATH = os.path.join(BASE_DIR, "data", "business_kb.json")
#
# _kb_cache = None
#
# def load_kb():
#     global _kb_cache
#
#     if _kb_cache is None:
#         if not os.path.exists(KB_PATH):
#             return {}
#
#         with open(KB_PATH, "r", encoding="utf-8") as f:
#             _kb_cache = json.load(f)
#
#     return _kb_cache
# import json
# import os
#
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# KB_PATH = os.path.join(BASE_DIR, "data", "business_kb.json")
#
# _kb_cache = None
#
# def load_kb():
#     global _kb_cache
#
#     if _kb_cache is None:
#         if not os.path.exists(KB_PATH):
#             return {}
#
#         with open(KB_PATH, "r", encoding="utf-8") as f:
#             _kb_cache = json.load(f)
#
#     return _kb_cache
# 2nd
# import json
# from pathlib import Path
#
# KB_PATH = Path(__file__).parent.parent / "data" / "business_kb.json"
#
# def load_kb():
#     if not KB_PATH.exists():
#         return None
#
#     with open(KB_PATH, "r", encoding="utf-8") as f:
#         return json.load(f)
# 3rd

import json
import os

# KB_PATH = "backend/app/data/business_kb.json"
#
#
# def load_kb():
#     if not os.path.exists(KB_PATH):
#         return {}
#
#     with open(KB_PATH, "r", encoding="utf-8") as f:
#         return json.load(f)
#
#
# def save_kb(data: dict):
#     os.makedirs(os.path.dirname(KB_PATH), exist_ok=True)
#
#     with open(KB_PATH, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)

# =================

import json
from pathlib import Path

BASE_KB_PATH = Path(__file__).resolve().parent.parent / "knowledge" / "mama_aisha_foods"

def load_json(file_name: str):
    file_path = BASE_KB_PATH / file_name
    if not file_path.exists():
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_kb():
    return {
        "profile": load_json("business_profile.json"),
        "menu": load_json("menu_and_pricing.json"),
        "delivery": load_json("delivery_and_location.json"),
        "hours": load_json("working_hours.json"),
        "faqs": load_json("faqs.json"),
        "orders": load_json("order_flow.json"),
        "complaints": load_json("complaints_and_support.json"),
        "business_tips": load_json("food_business_tips.json")
    }
