# Agentic DS + Quant Analytics Workflow

A terminal-first, natural-language analytics toolkit blueprint for orchestrating data cleaning, SQL access, and dashboard/report management across Tableau and presentation workflows.

## Product Vision

Build an **LLM-integrated (LI) orchestration agent** that coordinates specialized agents and tools so analysts can:

- Query and join data from SQL systems.
- Clean and transform datasets with reproducible pipelines.
- Generate and manage Tableau dashboards via validated schemas.
- Publish insights into reporting outputs (e.g., PowerPoint-ready artifacts).

## Build Milestones

### Short-Term Build

- Agent orchestration core for routing tasks to specialist agents.
- Data cleaning + transformation agent primitives.
- Prompt/response contracts for deterministic tool invocation.

### Intermediate Build

- Tableau dashboard generation using:
  - RAG knowledge base for dashboard patterns and data model context.
  - Pydantic validators to enforce valid dashboard structures/API payloads.
- SQL database integration layer with schema introspection and safe query execution.

### End Goal

A multi-platform toolkit where analysts can run natural-language commands in terminal workflows to query data, transform datasets, and manage dashboards/reports (Tableau, PowerPoint, and related formats).

## Repository Layout

- `docs/agentic_workflow_blueprint.md` — architecture, execution flow, and delivery roadmap.
- `agents/agent_registry.yaml` — role-to-agent mapping and ownership boundaries.
- `skills_library/` — reusable skill modules for each agent in the workflow.

## Quick Start for Contributors

1. Review `docs/agentic_workflow_blueprint.md`.
2. Update `agents/agent_registry.yaml` when adding or changing agents.
3. Add or edit agent skills under `skills_library/<agent-name>/SKILL.md`.
4. Keep skills concise, procedural, and tool-integrated.
