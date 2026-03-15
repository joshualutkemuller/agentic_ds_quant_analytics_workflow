from __future__ import annotations

from .contracts import AgentResponse, QueryPlan, UserRequest
from .data_prep import DataPrepAgent
from .eda import EDAAgent
from .llm import LLMConfig, LLMRouter
from .modes import resolve_mode
from .powerbi import PowerBIDashboardAgent, PowerBIPayloadValidator
from .rag import SimpleRAGStore
from .sql_tools import SQLIntegrationAgent
from .tableau import TableauDashboardAgent, TableauPayloadValidator


class LIOrchestratorAgent:
    """Natural-language orchestrator for SQL -> data prep -> EDA -> dashboard output."""

    def __init__(self, db_path: str, knowledge_base_path: str, llm_config: LLMConfig | None = None) -> None:
        self.sql_agent = SQLIntegrationAgent(db_path)
        self.prep_agent = DataPrepAgent()
        self.eda_agent = EDAAgent()
        self.rag = SimpleRAGStore(knowledge_base_path)
        self.tableau_agent = TableauDashboardAgent(TableauPayloadValidator())
        self.powerbi_agent = PowerBIDashboardAgent(PowerBIPayloadValidator())
        self.llm_router = LLMRouter(llm_config or LLMConfig())

    def run(self, request: UserRequest) -> AgentResponse:
        self.sql_agent.setup_demo_data()

        target = "powerbi" if "powerbi" in request.prompt.lower() else "tableau"
        workflow_mode = resolve_mode(request.prompt, request.mode)

        plan = QueryPlan(
            steps=[
                "sql-integration: query warehouse",
                "data-prep: clean and normalize rows",
                "eda-specialist: generate exploratory profile",
                f"{target}-dashboard: generate validated payload",
                "reporting: return terminal summary",
            ],
            metadata={
                "mode": workflow_mode.name,
                "mode_focus": workflow_mode.focus,
                "request": request.prompt,
                "target": target,
                "llm": self.llm_router.summary(),
            },
        )

        data = self.sql_agent.query("SELECT region, segment, sales, profit FROM sales")
        prepared = self.prep_agent.clean(data)
        eda = self.eda_agent.analyze(prepared)
        docs = self.rag.retrieve(request.prompt, top_k=2)

        tableau_dashboard = None
        powerbi_dashboard = None
        if target == "powerbi":
            powerbi_dashboard = self.powerbi_agent.build_payload(
                prompt=request.prompt,
                dataset="sqlite.sales",
                available_columns=list(prepared.schema.keys()),
                knowledge_docs=docs,
            )
        else:
            tableau_dashboard = self.tableau_agent.build_payload(
                prompt=request.prompt,
                datasource="sqlite.sales",
                available_columns=list(prepared.schema.keys()),
                knowledge_docs=docs,
            )

        report = (
            f"Generated {target} dashboard payload in {workflow_mode.name} mode. "
            f"Rows processed: {len(prepared.rows)}. "
            f"EDA insights: {len(eda.insights)}."
        )

        return AgentResponse(
            plan=plan,
            data=prepared,
            eda=eda,
            report=report,
            tableau_dashboard=tableau_dashboard,
            powerbi_dashboard=powerbi_dashboard,
        )
