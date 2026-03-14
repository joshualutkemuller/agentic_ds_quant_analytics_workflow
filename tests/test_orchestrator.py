from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from src.li_agent import LIOrchestratorAgent, UserRequest


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
        return LIOrchestratorAgent(db_path=db_path, knowledge_base_path=str(kb_path))

    def test_end_to_end_tableau_run(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            orchestrator = self._build_orchestrator(tmp)
            response = orchestrator.run(UserRequest(prompt="Build a regional sales dashboard"))

            self.assertEqual(len(response.plan.steps), 4)
            self.assertGreaterEqual(len(response.data.rows), 1)
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


if __name__ == "__main__":
    unittest.main()
