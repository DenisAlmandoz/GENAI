# Databricks GenAI Certification Practice Repo

This repository is a complete self-study workspace for the **Databricks Generative AI Engineer / GenAI certification study guide**. It is designed so you can practice every topic locally with **modular Python**, **bundled sample data**, and a **clear section-by-section roadmap**.

> Goal: help you move from “I know the topics” to “I can explain, design, and implement them like a Databricks GenAI practitioner.”

## What is included

- **A structured study map** covering all 6 sections of the guide.
- **Python modules** for prompts, chunking, retrieval evaluation, guardrails, deployment planning, monitoring, and model selection.
- **Bundled sample datasets** so you do not need to upload anything to start practicing.
- **Hands-on lab guides** in `docs/labs/` with exercises and self-checks.
- **Simple tests** so you can validate the repo setup quickly.

## Repository layout

```text
.
├── README.md
├── data/
│   └── raw/
│       ├── architecture_notes.md
│       ├── policies/policy_manual.md
│       └── product/catalog.json
├── docs/labs/
│   ├── section_1_design_applications.md
│   ├── section_2_data_preparation.md
│   ├── section_3_application_development.md
│   ├── section_4_assembling_and_deploying.md
│   ├── section_5_governance.md
│   └── section_6_evaluation_and_monitoring.md
├── src/databricks_genai_practice/
│   ├── catalog.py
│   ├── chunking.py
│   ├── data_quality.py
│   ├── deployment.py
│   ├── guardrails.py
│   ├── model_selection.py
│   ├── monitoring.py
│   ├── pipelines.py
│   ├── prompts.py
│   ├── retrieval_eval.py
│   ├── study_guide.py
│   └── tools.py
└── tests/test_catalog.py
```

## Quick start

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install the package in editable mode

```bash
pip install -e . --no-build-isolation
```

### 3. Run the tests

```bash
pytest
```

### 4. Print the full study plan

```bash
python - <<'PY'
from databricks_genai_practice.study_guide import quickstart
print(quickstart())
PY
```

## The easiest way to study

Follow this order exactly:

1. **Read this README once** to understand the structure.
2. **Run the quickstart command** to print the full learning plan.
3. **Complete one section at a time** using the corresponding file in `docs/labs/`.
4. **Inspect the matching Python modules** and modify them as you practice.
5. **Write your own notes** for every exercise: what input, what output, why that design.
6. **Repeat the labs until you can explain each answer without looking anything up.**

## Section-by-section learning path

### Section 1: Design Applications
Practice in:
- `docs/labs/section_1_design_applications.md`
- `src/databricks_genai_practice/prompts.py`
- `src/databricks_genai_practice/pipelines.py`
- `src/databricks_genai_practice/study_guide.py`

What you will master:
- Designing prompts that force a format.
- Choosing the right model task for a business need.
- Translating business goals into AI inputs/outputs.
- Choosing and ordering tools for multi-stage reasoning.

### Section 2: Data Preparation
Practice in:
- `docs/labs/section_2_data_preparation.md`
- `src/databricks_genai_practice/chunking.py`
- `src/databricks_genai_practice/data_quality.py`
- `src/databricks_genai_practice/retrieval_eval.py`
- `data/raw/policies/policy_manual.md`

What you will master:
- Chunking strategies for different source structures.
- Removing content that hurts RAG quality.
- Choosing extraction libraries by file type.
- Planning Delta Lake + Unity Catalog ingestion.
- Evaluating retrieval and explaining re-ranking.

### Section 3: Application Development
Practice in:
- `docs/labs/section_3_application_development.md`
- `src/databricks_genai_practice/tools.py`
- `src/databricks_genai_practice/prompts.py`
- `src/databricks_genai_practice/guardrails.py`
- `src/databricks_genai_practice/model_selection.py`

What you will master:
- Building tools for retrieval workflows.
- Adjusting prompts to improve output quality.
- Adding guardrails to reduce leakage and misuse.
- Selecting LLMs and embedding models using constraints and metrics.

### Section 4: Assembling and Deploying Applications
Practice in:
- `docs/labs/section_4_assembling_and_deploying.md`
- `src/databricks_genai_practice/pipelines.py`
- `src/databricks_genai_practice/deployment.py`
- `data/raw/architecture_notes.md`

What you will master:
- Coding simple chains.
- Understanding pyfunc packaging.
- Planning Vector Search and serving flows.
- Registering and serving governed RAG applications.

### Section 5: Governance
Practice in:
- `docs/labs/section_5_governance.md`
- `src/databricks_genai_practice/guardrails.py`
- `src/databricks_genai_practice/data_quality.py`
- `data/raw/policies/policy_manual.md`

What you will master:
- Masking techniques as guardrails.
- Malicious input protection.
- Licensing and legal-risk awareness.
- Mitigating problematic source text.

### Section 6: Evaluation and Monitoring
Practice in:
- `docs/labs/section_6_evaluation_and_monitoring.md`
- `src/databricks_genai_practice/retrieval_eval.py`
- `src/databricks_genai_practice/monitoring.py`
- `src/databricks_genai_practice/study_guide.py`

What you will master:
- Picking models from evaluation results.
- Monitoring deployed RAG systems.
- Using inference logging concepts.
- Comparing evaluation vs. monitoring in the lifecycle.

## How this repo covers every study-guide point

This repo covers the study guide in three layers:

1. **Conceptual coverage** through the lab instructions.
2. **Implementation coverage** through reusable Python modules.
3. **Practice coverage** through bundled datasets and exercises.

Use the mapping below when you want targeted revision:

- **Prompt design / output formatting** -> `prompts.py`
- **Business goal to task mapping** -> `catalog.py`, `study_guide.py`
- **Tool ordering / multi-stage reasoning** -> `pipelines.py`
- **Chunking and extraction** -> `chunking.py`, `data_quality.py`
- **Retrieval evaluation / re-ranking** -> `retrieval_eval.py`
- **Tool building** -> `tools.py`
- **Guardrails / masking / prompt injection** -> `guardrails.py`
- **Model and embedding selection** -> `model_selection.py`
- **Chain assembly / pyfunc / deployment flow** -> `deployment.py`, `pipelines.py`
- **Monitoring / inference logging / lifecycle thinking** -> `monitoring.py`, `study_guide.py`

## Bundled practice data

You asked for data so you do not need to upload anything. This repo includes:

- `data/raw/product/catalog.json`: business use cases to turn into solution designs.
- `data/raw/policies/policy_manual.md`: policy-style content for chunking, filtering, masking, and retrieval practice.
- `data/raw/architecture_notes.md`: architecture content for RAG, Vector Search, MLflow, and monitoring exercises.

## Recommended expert path

If you want to become truly strong, use this cadence:

### Pass 1: Foundations
- Read each lab.
- Run the helper functions.
- Make sure every concept is familiar.

### Pass 2: Explain everything out loud
- For every bullet in the certification guide, explain:
  - the business problem,
  - the right Databricks feature,
  - the pipeline input,
  - the pipeline output,
  - the evaluation metric,
  - the main risk.

### Pass 3: Build variants
- Add a second dataset.
- Create harder prompts.
- Introduce noisy data.
- Simulate bad retrieval and improve it.
- Add stricter guardrails.

### Pass 4: Mock exam mode
- Hide the code.
- Answer each study-guide bullet from memory.
- Then verify yourself against the labs and modules.

## Suggested next upgrades

Once you finish the base material, extend this repo with:

- a notebook version for Databricks workspace execution,
- MLflow experiment logging,
- synthetic evaluation datasets,
- a small local RAG demo,
- a mock agent with tool-calling traces,
- sample Delta Lake table schemas,
- sample Unity Catalog object naming standards.

## Important note

This repo is intentionally **practice-first** rather than tied to one exact vendor API. That is on purpose: certification success usually comes from understanding **how to reason about architecture, tradeoffs, safety, retrieval, deployment, and evaluation**, not just memorizing a single code path.

If you want, the next iteration can add:
- **Databricks notebook versions** of the labs,
- **MLflow examples**, 
- **Vector Search examples**,
- **mock certification quizzes**,
- or a **full end-to-end mini RAG app**.
