# 07 Counterparty Stress Early Warning

## Objective
Detect early stress in borrower counterparties using financing behavior, utilization shifts, and margin patterns.

## ML Design
- Primary model: **Temporal Fusion Transformer + Isolation Forest**
- Prediction target: `stress_event_next_5d`
- Cadence: 15-60 minute intraday scoring windows

## Deliverables
- `src/main.py` orchestration entry point
- Feature pipeline and model API in `src/`
- Alert routing for email/teams/webhooks
- PowerBI push + streaming publisher
- Unit tests under `tests/`
