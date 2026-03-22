from __future__ import annotations

from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class PracticeTask:
    objective: str
    deliverable: str
    module_hint: str


@dataclass(frozen=True)
class SectionPlan:
    title: str
    summary: str
    lab_file: str
    tasks: tuple[PracticeTask, ...]


SECTION_CATALOG: tuple[SectionPlan, ...] = (
    SectionPlan(
        title="Section 1: Design Applications",
        summary="Translate business goals into model tasks, prompts, tools, and chain design.",
        lab_file="docs/labs/section_1_design_applications.md",
        tasks=(
            PracticeTask("Design prompts for structured outputs.", "Create JSON and rubric-based prompts.", "prompts.py"),
            PracticeTask("Map business requirements to model tasks.", "Choose extraction, generation, routing, and agent tasks.", "study_guide.py"),
            PracticeTask("Order tools for multi-stage reasoning.", "Define retrieval, validation, and action steps.", "pipelines.py"),
        ),
    ),
    SectionPlan(
        title="Section 2: Data Preparation",
        summary="Prepare high-quality source content, chunking, embeddings, and Delta Lake ingestion plans.",
        lab_file="docs/labs/section_2_data_preparation.md",
        tasks=(
            PracticeTask("Apply chunking strategies.", "Compare fixed, semantic, and structure-aware chunking.", "chunking.py"),
            PracticeTask("Filter noisy content.", "Remove navigation, disclaimers, and duplicate boilerplate.", "data_quality.py"),
            PracticeTask("Evaluate retrieval.", "Score recall-style metrics and reranking impact.", "retrieval_eval.py"),
        ),
    ),
    SectionPlan(
        title="Section 3: Application Development",
        summary="Build tools, prompts, guardrails, and model selection logic for GenAI apps.",
        lab_file="docs/labs/section_3_application_development.md",
        tasks=(
            PracticeTask("Build retrieval and action tools.", "Implement modular callable tools.", "tools.py"),
            PracticeTask("Tune prompts and guardrails.", "Use metaprompts, templates, and policy checks.", "prompts.py"),
            PracticeTask("Choose models and embeddings.", "Compare constraints, context length, and quality metrics.", "model_selection.py"),
        ),
    ),
    SectionPlan(
        title="Section 4: Assembling and Deploying Applications",
        summary="Assemble chains, vector search, serving, MLflow packaging, and deployment steps.",
        lab_file="docs/labs/section_4_assembling_and_deploying.md",
        tasks=(
            PracticeTask("Code simple chains.", "Implement pre-processing, retrieval, generation, and post-processing.", "pipelines.py"),
            PracticeTask("Plan Databricks deployment.", "Sequence Vector Search, UC, Model Serving, and endpoint controls.", "study_guide.py"),
            PracticeTask("Serve RAG workloads.", "Specify model flavor, dependencies, signatures, and endpoint needs.", "deployment.py"),
        ),
    ),
    SectionPlan(
        title="Section 5: Governance",
        summary="Reduce legal, privacy, and prompt-injection risk with guardrails and data governance.",
        lab_file="docs/labs/section_5_governance.md",
        tasks=(
            PracticeTask("Apply masking and input protections.", "Mask sensitive data and reject malicious requests.", "guardrails.py"),
            PracticeTask("Assess source licensing.", "Identify allowed and risky data sources.", "data_quality.py"),
        ),
    ),
    SectionPlan(
        title="Section 6: Evaluation and Monitoring",
        summary="Evaluate RAG quality, monitor costs, compare models, and use Databricks observability features.",
        lab_file="docs/labs/section_6_evaluation_and_monitoring.md",
        tasks=(
            PracticeTask("Choose evaluation metrics.", "Link scenario goals to quantitative and qualitative metrics.", "retrieval_eval.py"),
            PracticeTask("Monitor live systems.", "Define inference logging, cost, latency, and safety checks.", "monitoring.py"),
            PracticeTask("Compare lifecycle phases.", "Explain evaluation vs. monitoring responsibilities.", "study_guide.py"),
        ),
    ),
)


def build_study_plan() -> str:
    lines = ["Databricks GenAI Certification Practice Plan", "=" * 43, ""]
    for section in SECTION_CATALOG:
        lines.append(f"{section.title} — {section.summary}")
        for task in section.tasks:
            lines.append(f"  - Objective: {task.objective}")
            lines.append(f"    Deliverable: {task.deliverable}")
            lines.append(f"    Start in module: {task.module_hint}")
        lines.append(f"  - Guided lab: {section.lab_file}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    print(build_study_plan())
