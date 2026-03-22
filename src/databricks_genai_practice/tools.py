from __future__ import annotations

from pathlib import Path


def load_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def keyword_lookup(text: str, term: str) -> list[str]:
    return [line for line in text.splitlines() if term.lower() in line.lower()]


def summarize_fields(record: dict[str, str], fields: list[str]) -> str:
    return " | ".join(f"{field}: {record.get(field, 'n/a')}" for field in fields)
