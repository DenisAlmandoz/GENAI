# Databricks notebook source
# Section 5 Lab - Governance
# Mirrors docs/labs/section_5_governance.md

# COMMAND ----------
%pip install -e . --no-build-isolation

# COMMAND ----------
from pathlib import Path
repo = Path("/Workspace/Users/ynwa_07@hotmail.com/GENAI")
policy_text = (repo / "data/raw/policies/policy_manual.md").read_text()

# COMMAND ----------
# Guardrails + masking
from databricks_genai_practice.guardrails import redact_sensitive_terms

redacted = redact_sensitive_terms(policy_text)
print(redacted[:1000])

# COMMAND ----------
# Data quality / governance checks
from databricks_genai_practice.data_quality import governance_risk_flags

flags = governance_risk_flags(policy_text)
flags
