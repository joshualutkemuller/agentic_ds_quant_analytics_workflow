from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from src.li_agent import LIOrchestratorAgent, UserRequest


class TestLIOrchestrator(unittest.TestCase):
    def test_end_to_end_run(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
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

            orchestrator = LIOrchestratorAgent(db_path=db_path, knowledge_base_path=str(kb_path))
            response = orchestrator.run(UserRequest(prompt="Build a regional sales dashboard"))

            self.assertEqual(len(response.plan.steps), 4)
            self.assertGreaterEqual(len(response.data.rows), 1)
            self.assertTrue(response.dashboard.metrics)
            self.assertTrue(response.dashboard.dimensions)
            self.assertIn("Rows processed", response.report)


if __name__ == "__main__":
    unittest.main()
