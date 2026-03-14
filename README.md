# Agentic DS + Quant Analytics Workflow

A terminal-first, natural-language analytics toolkit blueprint for orchestrating data cleaning, SQL access, and dashboard/report management across Tableau and presentation workflows.

## Product Vision

Build an **LLM-integrated (LI) orchestration agent** that coordinates specialized agents and tools so analysts can:

- Query and join data from SQL systems.
- Clean and transform datasets with reproducible pipelines.
- Generate and manage Tableau and PowerBI dashboards via validated schemas.
- Publish insights into reporting outputs (e.g., PowerPoint-ready artifacts).

## Build Milestones

### Short-Term Build

- Agent orchestration core for routing tasks to specialist agents.
- Data cleaning + transformation agent primitives.
- Prompt/response contracts for deterministic tool invocation.

### Intermediate Build

- Tableau dashboard generation using:
  - RAG knowledge base for dashboard patterns and data model context.
  - Pydantic-style validators to enforce valid dashboard structures/API payloads.
- SQL database integration layer with schema introspection and safe query execution.

### End Goal

A multi-platform toolkit where analysts can run natural-language commands in terminal workflows to query data, transform datasets, and manage dashboards/reports (Tableau, PowerPoint, and related formats).

## What Is Implemented Now

This repository now includes a runnable **starter LI orchestrator** that executes a short-term flow:

1. SQL Integration Agent loads/query demo warehouse data.
2. Data Prep Agent performs deterministic cleaning.
3. Tableau Dashboard Agent retrieves guidance from a local RAG knowledge file.
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

## Repository Layout

- `docs/agentic_workflow_blueprint.md` — architecture, execution flow, and delivery roadmap.
- `agents/agent_registry.yaml` — role-to-agent mapping and ownership boundaries.
- `skills_library/` — reusable skill modules for each agent in the workflow.
- `src/li_agent/` — runnable orchestration prototype code.
- `cli.py` — terminal entry point.
- `tests/` — baseline unit tests.

## Quick Start for Contributors

1. Review `docs/agentic_workflow_blueprint.md`.
2. Update `agents/agent_registry.yaml` when adding or changing agents.
3. Add or edit agent skills under `skills_library/<agent-name>/SKILL.md`.
4. Extend `src/li_agent/` modules for production tool adapters (Tableau API, PowerBI API, PowerPoint exporters, production SQL connectors).
