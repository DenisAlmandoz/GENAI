# Databricks notebook source
# Section 2 Lab - Data Preparation
# Mirrors docs/labs/section_2_data_preparation.md

# COMMAND ----------
%pip install -e . --no-build-isolation

# COMMAND ----------
# Load policy manual text
from pathlib import Path

repo = Path("/Workspace/Users/ynwa_07@hotmail.com/GENAI")
policy_text = (repo / "data/raw/policies/policy_manual.md").read_text()
print(policy_text[:1000])

# COMMAND ----------
# Explore chunking strategies
from databricks_genai_practice.chunking import simple_chunk, chunk_by_headings

# TODO: choose a chunking method and inspect results
chunks = simple_chunk(policy_text, chunk_size=500)
print(chunks[0])

# COMMAND ----------
# Data quality checks
from databricks_genai_practice.data_quality import find_issues

issues = find_issues(policy_text)
issues

# COMMAND ----------
# Retrieval evaluation basics
from databricks_genai_practice.retrieval_eval import make_retrieval_plan

plan = make_retrieval_plan("policy compliance FAQ")
print(plan)
