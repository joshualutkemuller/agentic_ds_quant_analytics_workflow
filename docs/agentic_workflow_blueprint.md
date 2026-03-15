# Agentic Workflow Blueprint

## 1) System Objective

Design a command-line analytics copilot that turns natural-language user intents into reliable data and dashboard operations by coordinating specialist agents.

## 2) Core Agent Topology

1. **Orchestrator Agent**
   - Interprets intent, selects mode, decomposes tasks, chooses execution path.
2. **Data Prep Agent**
   - Cleans, normalizes, and transforms datasets.
3. **EDA Specialist Agent**
   - Produces exploratory profiles and numeric summaries before dashboard generation.
4. **SQL Integration Agent**
   - Connects to SQL systems, profiles schemas, executes guarded queries.
5. **Tableau Dashboard Agent**
   - Generates Tableau dashboard specs with RAG context and validator checks.
6. **PowerBI Dashboard Agent**
   - Generates and manages PowerBI report/dashboard specs with schema validation.
7. **Reporting Agent**
   - Converts dashboard/data outputs into consumable report artifacts.
8. **Quality Guard Agent**
   - Validates payloads, enforces contracts, tracks observability metrics.

## 3) Execution Lifecycle

1. Intent capture from terminal.
2. Mode selection and task planning by Orchestrator.
3. Data access via SQL Integration Agent.
4. Data cleaning/transformation via Data Prep Agent.
5. Exploratory analysis via EDA Specialist Agent.
6. Dashboard generation via Tableau or PowerBI Dashboard Agent.
7. Validation and policy checks by Quality Guard Agent.
8. Reporting/export actions via Reporting Agent.
9. Artifact summary returned to user in terminal.

## 4) Analytical Modes

The orchestrator can run with explicit specializations:

- `general`
- `portfolio_management`
- `securities_lending_collateral`
- `sales_specialist`
- `broad_data_scientist`

Modes steer planning context, summary emphasis, and downstream dashboard/report focus.

## 5) LLM Routing

The scaffold supports provider-agnostic LLM metadata routing:

- default deterministic mode (`provider=none`)
- configurable provider/model labels (`openai`, `anthropic`, `local`, `langchain`, etc.)
- metadata propagation to execution plan for observability

## 6) RAG + Validation Pattern for Dashboarding

- Index reusable dashboard patterns, schema docs, and prior templates.
- Retrieve top-k context relevant to user request.
- Produce structured dashboard payload.
- Validate with Pydantic contracts before any API submission.
- Auto-repair invalid payloads through bounded retry loop.

## 7) Current Implementation Slice

The repository currently ships a runnable short-term scaffold in `src/li_agent/`:

- Local SQLite SQL integration (`sql_tools.py`) with demo data bootstrap.
- Deterministic cleaning pass (`data_prep.py`).
- EDA report generation (`eda.py`).
- File-backed lightweight retrieval store (`rag.py`).
- Tableau payload generation + validation (`tableau.py`) with optional Pydantic usage.
- PowerBI payload generation + validation (`powerbi.py`) with optional Pydantic usage.
- Provider-agnostic LLM config/routing metadata (`llm.py`).
- Mode resolution logic (`modes.py`).
- End-to-end orchestrator (`orchestrator.py`) and CLI entrypoint (`cli.py`).

## 8) Recommended Interfaces

- Agent-to-agent contract format: JSON schema typed envelopes.
- Skill library format: per-agent `SKILL.md` with deterministic workflow steps.
- Tool adapters: SQL client, Tableau API wrapper, PowerBI API wrapper, report exporter.

## 9) Delivery Roadmap

### Phase A (Short-Term)
- Orchestrator, Data Prep, EDA, and base SQL execution flow.
- Minimal CLI and prompt contracts.

### Phase B (Intermediate)
- Full Tableau/PowerBI generation path with RAG + Pydantic guardrails.
- Schema-aware query planning and reusable transformations.
- Production SQL connectors and governed query templates.
- LangChain or direct SDK adapters for selected LLM providers.

### Phase C (End State)
- Multi-platform outputs (Tableau + PowerPoint/reporting channels).
- Persistent memory of analytical workflows and reusable playbooks.
