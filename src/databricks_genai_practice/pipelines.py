from __future__ import annotations

from .data_quality import filter_extraneous_lines
from .chunking import markdown_heading_chunks


def rag_preprocess(text: str) -> list[str]:
    cleaned = filter_extraneous_lines(text)
    return [chunk.text for chunk in markdown_heading_chunks(cleaned)]


def tool_order() -> list[str]:
    return [
        "classify intent",
        "retrieve relevant documents",
        "rerank evidence",
        "run policy guardrails",
        "generate grounded answer",
        "post-process structured output",
    ]
