from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelCard:
    name: str
    strengths: tuple[str, ...]
    context_window: int
    latency_tier: str
    best_for: tuple[str, ...]


MODEL_CARDS = (
    ModelCard("databricks-dbrx-instruct", ("reasoning", "tool use"), 32768, "medium", ("agent", "rag")),
    ModelCard("llama-3.1-70b-instruct", ("generation", "instruction following"), 131072, "slow", ("rag", "chat")),
    ModelCard("gte-large-en", ("embeddings",), 8192, "fast", ("retrieval",)),
)


def select_models(task: str) -> list[ModelCard]:
    task_lower = task.lower()
    return [card for card in MODEL_CARDS if task_lower in card.best_for]
