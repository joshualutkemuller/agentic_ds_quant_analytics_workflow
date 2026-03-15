from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class UserRequest:
    """Natural-language request accepted by the CLI."""

    prompt: str
    output_format: str = "terminal"
    mode: Optional[str] = None


@dataclass
class QueryPlan:
    """Execution plan produced by the orchestrator."""

    steps: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DataArtifact:
    """Normalized dataset representation shared between agents."""

    rows: List[Dict[str, Any]]
    schema: Dict[str, str]
    lineage: List[str] = field(default_factory=list)


@dataclass
class EDAReport:
    """Exploratory data analysis output."""

    row_count: int
    columns: List[str]
    numeric_profile: Dict[str, Dict[str, float]]
    insights: List[str]


@dataclass
class DashboardPayload:
    """Structured Tableau payload."""

    title: str
    datasource: str
    worksheet: str
    metrics: List[str]
    dimensions: List[str]
    filters: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PowerBIPayload:
    """Structured PowerBI report payload."""

    title: str
    dataset: str
    report_page: str
    visuals: List[str]
    measures: List[str]
    filters: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentResponse:
    """Final response returned by orchestrator."""

    plan: QueryPlan
    data: DataArtifact
    eda: EDAReport
    report: str
    tableau_dashboard: Optional[DashboardPayload] = None
    powerbi_dashboard: Optional[PowerBIPayload] = None
