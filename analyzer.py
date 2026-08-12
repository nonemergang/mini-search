import re

def analyze_document(text:str) -> list[str]:
    normalized_text = text.lower()
    normalized_text = re.sub(r"[^\w\s]", "", normalized_text)

    return normalized_text.split()