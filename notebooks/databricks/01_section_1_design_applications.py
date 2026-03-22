# Databricks notebook source
# Section 1 Lab - Design Applications
# This notebook mirrors docs/labs/section_1_design_applications.md

# COMMAND ----------
# Setup
# If running from Databricks Repos, this installs the package in editable mode.
%pip install -e . --no-build-isolation

# COMMAND ----------
# Step 1: Open data/raw/product/catalog.json and choose one business use case
from pathlib import Path

repo = Path("/Workspace/Users/ynwa_07@hotmail.com/GENAI")
raw_catalog = (repo / "data/raw/product/catalog.json").read_text()
print(raw_catalog[:1000])

# TODO: Pick one use case from the JSON above and paste it below.
chosen_use_case = ""  # e.g., "Support ticket triage" or similar
print(chosen_use_case)

# COMMAND ----------
# Step 2: Write a structured prompt using structured_extraction_prompt()
from databricks_genai_practice.prompts import structured_extraction_prompt

prompt = structured_extraction_prompt()
print(prompt)

# TODO: If desired, adapt the prompt to your chosen use case.

# COMMAND ----------
# Step 3: Define required inputs, expected outputs, decision owner, success metric
# TODO: Fill these out for the chosen use case.
use_case_design = {
    "required_inputs": [],
    "expected_outputs": [],
    "decision_owner": "",
    "success_metric": "",
}
use_case_design

# COMMAND ----------
# Step 4: Use tool_order() and explain why each step is in that order
from databricks_genai_practice.pipelines import tool_order

order = tool_order()
print(order)

# TODO: Explain why each step is ordered this way, in plain text below.

# COMMAND ----------
# Step 5: Create your own JSON schema for a tool-calling agent response
# TODO: Replace this with your own schema tailored to the chosen use case.
response_schema = {
    "type": "object",
    "properties": {
        "action": {"type": "string"},
        "reason": {"type": "string"},
        "result": {"type": "object"},
    },
    "required": ["action", "result"],
}
response_schema
