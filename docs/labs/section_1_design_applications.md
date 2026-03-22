# Section 1 Lab - Design Applications

## What you will practice
- Designing prompts that force specific formats.
- Mapping business requirements to model tasks.
- Describing AI pipeline inputs, outputs, and tools.
- Sequencing tool use for multi-stage reasoning.

## Exercises
1. Open `data/raw/product/catalog.json` and choose one business use case.
2. Write a structured prompt using `structured_extraction_prompt()` in `src/databricks_genai_practice/prompts.py`.
3. For the chosen use case, define:
   - required inputs
   - expected outputs
   - decision owner
   - success metric
4. Use `tool_order()` in `src/databricks_genai_practice/pipelines.py` and explain why each step is in that order.
5. Create your own JSON schema for a tool-calling agent response.

## Check yourself
- Did you distinguish retrieval from generation?
- Did your prompt specify output schema and constraints?
- Did your tool order include validation before the final answer?
