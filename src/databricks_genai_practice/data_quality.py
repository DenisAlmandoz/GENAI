from __future__ import annotations

NOISE_MARKERS = (
    "cookie policy",
    "subscribe to our newsletter",
    "all rights reserved",
    "navigation menu",
)


def filter_extraneous_lines(text: str) -> str:
    kept = []
    for line in text.splitlines():
        lowered = line.strip().lower()
        if lowered and not any(marker in lowered for marker in NOISE_MARKERS):
            kept.append(line)
    return "\n".join(kept)


def recommend_extractor(file_type: str) -> str:
    mapping = {
        "pdf": "pymupdf",
        "html": "beautifulsoup4",
        "docx": "python-docx",
        "pptx": "python-pptx",
        "json": "json",
    }
    return mapping.get(file_type.lower(), "unstructured")
