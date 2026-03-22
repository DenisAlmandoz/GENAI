# Databricks notebook source
# Section 6 Lab - Evaluation and Monitoring
# Mirrors docs/labs/section_6_evaluation_and_monitoring.md

# COMMAND ----------
%pip install -e . --no-build-isolation

# COMMAND ----------
from databricks_genai_practice.retrieval_eval import eval_retrieval
from databricks_genai_practice.monitoring import monitoring_checklist

print(eval_retrieval("policy compliance"))
print(monitoring_checklist())
