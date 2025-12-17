from collections import Counter
from .memory_store import load_conversations


def summarize_conversations():
    data = load_conversations()

    user_msgs = [d["text"] for d in data if d["role"] == "user"]

    keywords = []
    for msg in user_msgs:
        keywords.extend(msg.lower().split())

    common = Counter(keywords).most_common(10)

    return {
        "total_messages": len(data),
        "top_keywords": common,
        "sample_questions": user_msgs[:5]
    }
