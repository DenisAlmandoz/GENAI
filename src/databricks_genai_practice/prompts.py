from __future__ import annotations

from textwrap import dedent


def structured_extraction_prompt(user_request: str) -> str:
    return dedent(
        f"""
        You are an AI solution architect for Databricks.
        Convert the request below into strict JSON with keys:
        business_goal, model_tasks, required_inputs, expected_outputs, risks, success_metrics.

        Request: {user_request}

        Rules:
        - Return valid JSON only.
        - Each model_tasks item must be one of: classification, extraction, summarization,
          retrieval, generation, tool_calling, evaluation.
        - expected_outputs must describe schema, format, and decision owner.
        """
    ).strip()


BASELINE_PROMPT = dedent(
    """
    Answer the user's question using the available context.
    If the answer is unsupported, say you need more evidence.
    Cite the supporting document ids in brackets.
    """
).strip()


GUARDRAIL_METAPROMPT = dedent(
    """
    Before answering, check whether the request asks for secrets, credentials,
    private personal data, or unsafe instructions. If yes, refuse briefly and offer a safe alternative.
    Otherwise answer using only grounded evidence from the retrieved context.
    """
).strip()
