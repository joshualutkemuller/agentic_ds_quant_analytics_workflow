# Agentic DS + Quant Analytics Workflow

A terminal-first, natural-language analytics toolkit blueprint for orchestrating data cleaning, SQL access, EDA, and dashboard/report management across Tableau, PowerBI, and presentation workflows.

## Product Vision

Build an **LLM-integrated (LI) orchestration agent** that coordinates specialized agents and tools so analysts can:

- Query and join data from SQL systems.
- Clean and transform datasets with reproducible pipelines.
- Run exploratory data analysis (EDA) using a specialist agent.
- Generate and manage Tableau and PowerBI dashboards via validated schemas.
- Publish insights into reporting outputs (e.g., PowerPoint-ready artifacts).

## Build Milestones

### Short-Term Build

- Agent orchestration core for routing tasks to specialist agents.
- Data cleaning + transformation + EDA agent primitives.
- Prompt/response contracts for deterministic tool invocation.

### Intermediate Build

- Tableau/PowerBI dashboard generation using:
  - RAG knowledge base for dashboard patterns and data model context.
  - Pydantic-style validators to enforce valid dashboard structures/API payloads.
- SQL database integration layer with schema introspection and safe query execution.
- Optional LLM provider adapters (OpenAI, Anthropic, LangChain, local).

### End Goal

A multi-platform toolkit where analysts can run natural-language commands in terminal workflows to query data, transform datasets, perform EDA, and manage dashboards/reports (Tableau, PowerBI, PowerPoint, and related formats).

## What Is Implemented Now

This repository includes a runnable **starter LI orchestrator** that executes:

1. SQL Integration Agent loads/query demo warehouse data.
2. Data Prep Agent performs deterministic cleaning.
3. EDA Specialist Agent produces exploratory summaries/statistics.
4. Tableau or PowerBI payload is generated from retrieved guidance.
5. Dashboard payload is validated (Pydantic if installed, strict fallback otherwise).
6. A terminal-ready report summary is returned.

## Run the Prototype

```bash
python cli.py "Build a regional sales dashboard with profit trends"
```

Optional flags:

- `--db data/demo.sqlite` (SQLite file path)
- `--kb data/tableau_knowledge.json` (RAG knowledge base JSON)
- `--mode <workflow_mode>` (analytical specialization)
- `--llm-provider <provider>` (e.g., `none`, `openai`, `anthropic`, `local`, `langchain`)
- `--llm-model <model_name>`

## LLM + Mode Configuration

- Default execution is deterministic scaffold mode (`--llm-provider none`).
- You can set provider metadata for future adapters (including LangChain) with `--llm-provider` and `--llm-model`.
- You can select analytical specializations with `--mode`:
  - `general`
  - `portfolio_management`
  - `securities_lending_collateral`
  - `sales_specialist`
  - `broad_data_scientist`

See `docs/llm_and_modes.md` for examples.

## Repository Layout

- `docs/agentic_workflow_blueprint.md` — architecture, execution flow, and delivery roadmap.
- `docs/running_samples.md` — step-by-step sample runs and output capture instructions.
- `docs/llm_and_modes.md` — LLM provider setup notes and analytical workflow mode usage.
- `agents/agent_registry.yaml` — role-to-agent mapping and ownership boundaries.
- `skills_library/` — reusable skill modules for each agent in the workflow.
- `src/li_agent/` — runnable orchestration prototype code.
- `cli.py` — terminal entry point.
- `tests/` — baseline unit tests.

## Quick Start for Contributors

1. Review `docs/agentic_workflow_blueprint.md`.
2. Update `agents/agent_registry.yaml` when adding or changing agents.
3. Add or edit agent skills under `skills_library/<agent-name>/SKILL.md`.
4. Extend `src/li_agent/` modules for production tool adapters (Tableau API, PowerBI API, PowerPoint exporters, production SQL connectors, and LLM runtime integrations).
