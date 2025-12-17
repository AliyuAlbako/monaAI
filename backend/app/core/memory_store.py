import json
import os
from datetime import datetime

DATA_PATH = "backend/app/data/conversations.json"


def save_message(session_id: str, role: str, text: str):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump([], f)

    with open(DATA_PATH, "r") as f:
        data = json.load(f)

    data.append({
        "session_id": session_id,
        "role": role,
        "text": text,
        "timestamp": datetime.utcnow().isoformat()
    })

    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)


def load_conversations():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)
import json
import os
from datetime import datetime

DATA_PATH = "backend/app/data/conversations.json"


def save_message(session_id: str, role: str, text: str):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump([], f)

    with open(DATA_PATH, "r") as f:
        data = json.load(f)

    data.append({
        "session_id": session_id,
        "role": role,
        "text": text,
        "timestamp": datetime.utcnow().isoformat()
    })

    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)


def load_conversations():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)
