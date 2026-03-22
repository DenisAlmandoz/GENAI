from __future__ import annotations

import re

EMAIL_RE = re.compile(r"\b[\w.-]+@[\w.-]+\.\w+\b")
SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")


def mask_sensitive_text(text: str) -> str:
    text = EMAIL_RE.sub("[EMAIL]", text)
    return SSN_RE.sub("[SSN]", text)


def looks_malicious(prompt: str) -> bool:
    lowered = prompt.lower()
    signals = ["ignore previous instructions", "reveal the system prompt", "print secrets"]
    return any(signal in lowered for signal in signals)
