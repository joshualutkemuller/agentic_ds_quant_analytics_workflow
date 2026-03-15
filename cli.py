from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from src.li_agent import LIOrchestratorAgent, LLMConfig, UserRequest


def main() -> None:
    parser = argparse.ArgumentParser(description="LI analytics orchestrator prototype")
    parser.add_argument("prompt", help="Natural-language analytics request")
    parser.add_argument("--db", default="data/demo.sqlite", help="Path to local sqlite database")
    parser.add_argument(
        "--kb",
        default="data/tableau_knowledge.json",
        help="Path to dashboard knowledge-base json",
    )
    parser.add_argument(
        "--mode",
        default=None,
        choices=[
            "general",
            "portfolio_management",
            "securities_lending_collateral",
            "sales_specialist",
            "broad_data_scientist",
        ],
        help="Optional analytical workflow mode",
    )
    parser.add_argument("--llm-provider", default="none", help="LLM provider label (openai/anthropic/local/langchain/etc)")
    parser.add_argument("--llm-model", default="", help="Model name for selected provider")
    args = parser.parse_args()

    orchestrator = LIOrchestratorAgent(
        db_path=args.db,
        knowledge_base_path=args.kb,
        llm_config=LLMConfig(provider=args.llm_provider, model=args.llm_model),
    )
    response = orchestrator.run(UserRequest(prompt=args.prompt, mode=args.mode))
    print(json.dumps(asdict(response), indent=2))


if __name__ == "__main__":
    main()
