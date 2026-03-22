# Databricks notebook source
# Section 4 Lab - Assembling and Deploying Applications
# Mirrors docs/labs/section_4_assembling_and_deploying.md

# COMMAND ----------
%pip install -e . --no-build-isolation

# COMMAND ----------
# Load architecture notes
from pathlib import Path
repo = Path("/Workspace/Users/ynwa_07@hotmail.com/GENAI")
notes = (repo / "data/raw/architecture_notes.md").read_text()
print(notes[:1000])

# COMMAND ----------
# Pipeline assembly
from databricks_genai_practice.pipelines import build_chain

chain = build_chain()
print(chain)

# COMMAND ----------
# Deployment planning
from databricks_genai_practice.deployment import deployment_plan

plan = deployment_plan("rag_app")
print(plan)
