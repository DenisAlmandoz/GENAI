# Section 3 Lab - Application Development

## What you will practice
- Tool creation for retrieval needs.
- Prompt adjustment and guardrails.
- Model and embedding selection.
- Qualitative response review.
- Agent prompt template design.

## Exercises
1. Build a retrieval helper with `load_text()` and `keyword_lookup()`.
2. Compare `BASELINE_PROMPT` and `GUARDRAIL_METAPROMPT`; explain how the output behavior changes.
3. Test `looks_malicious()` with both benign and malicious prompts.
4. Use `select_models()` to pick a model for `rag`, `agent`, and `retrieval`.
5. Draft an agent system prompt that exposes the available tools and refusal rules.
6. Review two sample answers and identify quality, safety, or grounding issues.

## Check yourself
- Did you choose an embedding model with enough context length for your chunking plan?
- Did you describe how prompt formatting changes output reliability?
- Did you include hallucination-minimizing instructions?
