# Databricks notebook source
# Section 3 Lab - Application Development
# Mirrors docs/labs/section_3_application_development.md

# COMMAND ----------
%pip install -e . --no-build-isolation

# COMMAND ----------
# Tools + prompts
from databricks_genai_practice.tools import tool_catalog
from databricks_genai_practice.prompts import structured_extraction_prompt

print(tool_catalog())
print(structured_extraction_prompt())

# COMMAND ----------
# Guardrails + model selection
from databricks_genai_practice.guardrails import basic_guardrail_rules
from databricks_genai_practice.model_selection import choose_model

print(basic_guardrail_rules())
print(choose_model(task="summarization", latency_ms=500, budget_usd=0.02))
