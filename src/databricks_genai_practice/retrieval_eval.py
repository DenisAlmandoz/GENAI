from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievalResult:
    query: str
    expected_doc_ids: tuple[str, ...]
    returned_doc_ids: tuple[str, ...]


def hit_rate_at_k(result: RetrievalResult, k: int) -> float:
    return float(any(doc_id in result.returned_doc_ids[:k] for doc_id in result.expected_doc_ids))


def mean_hit_rate(results: list[RetrievalResult], k: int) -> float:
    if not results:
        return 0.0
    return sum(hit_rate_at_k(result, k) for result in results) / len(results)


def reranking_note() -> str:
    return (
        "Re-ranking improves retrieval precision by reordering initially retrieved chunks "
        "with a stronger relevance model before generation."
    )
