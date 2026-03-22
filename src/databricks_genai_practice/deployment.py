from __future__ import annotations


def deployment_sequence() -> list[str]:
    return [
        "Prepare chunked source data and embeddings.",
        "Write chunks into Delta tables in Unity Catalog.",
        "Create and validate a Vector Search index.",
        "Package the chain with MLflow including dependencies and input examples.",
        "Register the model to Unity Catalog.",
        "Deploy a serving endpoint and configure access controls.",
        "Enable inference logging, evaluation, and cost monitoring.",
    ]
