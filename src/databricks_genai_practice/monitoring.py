from __future__ import annotations


def monitoring_metrics() -> list[str]:
    return [
        "answer groundedness",
        "retrieval hit rate",
        "latency p95",
        "tokens per request",
        "cost per successful task",
        "safety refusal rate",
        "user satisfaction",
    ]
