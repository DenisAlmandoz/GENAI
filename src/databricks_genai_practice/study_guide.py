from __future__ import annotations

from .catalog import build_study_plan
from .deployment import deployment_sequence
from .monitoring import monitoring_metrics
from .pipelines import tool_order


def quickstart() -> str:
    parts = [
        build_study_plan(),
        "Deployment sequence:\n- " + "\n- ".join(deployment_sequence()),
        "Recommended tool order:\n- " + "\n- ".join(tool_order()),
        "Monitoring metrics:\n- " + "\n- ".join(monitoring_metrics()),
    ]
    return "\n\n".join(parts)
