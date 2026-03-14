from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from src.li_agent import LIOrchestratorAgent, UserRequest


def main() -> None:
    parser = argparse.ArgumentParser(description="LI analytics orchestrator prototype")
    parser.add_argument("prompt", help="Natural-language analytics request")
    parser.add_argument("--db", default="data/demo.sqlite", help="Path to local sqlite database")
    parser.add_argument(
        "--kb",
        default="data/tableau_knowledge.json",
        help="Path to dashboard knowledge-base json",
    )
    args = parser.parse_args()

    orchestrator = LIOrchestratorAgent(db_path=args.db, knowledge_base_path=args.kb)
    response = orchestrator.run(UserRequest(prompt=args.prompt))
    print(json.dumps(asdict(response), indent=2))


if __name__ == "__main__":
    main()
