def detect_language(text: str) -> str:
    text = text.lower()

    hausa = ["ina", "ya kake", "yaya", "lafiya", "don allah", "na gode"]
    yoruba = ["bawo", "se daadaa", "inu", "e kaaro", "eko", "bẹẹni"]
    igbo = ["kedu", "ịnọ", "ụtụtụ", "daalụ", "biko", "ụtụtụ ọma"]
    pidgin = ["how far", "wetin", "abeg", "dey", "na so"]

    if any(word in text for word in hausa):
        return "ha"
    if any(word in text for word in yoruba):
        return "yo"
    if any(word in text for word in igbo):
        return "ig"
    if any(word in text for word in pidgin):
        return "pidgin"

    return "en"
