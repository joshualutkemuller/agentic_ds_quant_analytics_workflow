from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from src.li_agent import LIOrchestratorAgent, UserRequest
from src.li_agent.llm import LLMConfig


class TestLIOrchestrator(unittest.TestCase):
    def _build_orchestrator(self, tmp: str) -> LIOrchestratorAgent:
        db_path = str(Path(tmp) / "demo.sqlite")
        kb_path = Path(tmp) / "kb.json"
        kb_path.write_text(
            json.dumps(
                [
                    {
                        "title": "Regional Sales Overview",
                        "tags": ["region", "sales"],
                        "content": "Use sales and profit by region.",
                    }
                ]
            )
        )
        return LIOrchestratorAgent(
            db_path=db_path,
            knowledge_base_path=str(kb_path),
            llm_config=LLMConfig(provider="langchain", model="gpt-4o-mini"),
        )

    def test_end_to_end_tableau_run(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            orchestrator = self._build_orchestrator(tmp)
            response = orchestrator.run(UserRequest(prompt="Build a regional sales dashboard"))

            self.assertEqual(len(response.plan.steps), 5)
            self.assertGreaterEqual(len(response.data.rows), 1)
            self.assertIsNotNone(response.eda)
            self.assertIsNotNone(response.tableau_dashboard)
            self.assertIsNone(response.powerbi_dashboard)
            self.assertTrue(response.tableau_dashboard.metrics)
            self.assertIn("Rows processed", response.report)

    def test_end_to_end_powerbi_run(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            orchestrator = self._build_orchestrator(tmp)
            response = orchestrator.run(UserRequest(prompt="Build a PowerBI dashboard for regional performance"))

            self.assertEqual(response.plan.metadata["target"], "powerbi")
            self.assertIsNone(response.tableau_dashboard)
            self.assertIsNotNone(response.powerbi_dashboard)
            self.assertTrue(response.powerbi_dashboard.measures)

    def test_portfolio_mode_selection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            orchestrator = self._build_orchestrator(tmp)
            response = orchestrator.run(
                UserRequest(
                    prompt="Build a portfolio analytics dashboard for client exposures",
                    mode="portfolio_management",
                )
            )
            self.assertEqual(response.plan.metadata["mode"], "portfolio_management")
            self.assertIn("LLM provider", response.plan.metadata["llm"])


if __name__ == "__main__":
    unittest.main()
