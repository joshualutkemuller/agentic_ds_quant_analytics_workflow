# 08 Inventory Recall Pressure Nowcaster

## Objective
Nowcast near-term inventory recall pressure driven by corporate actions, specials, and demand imbalance.

## ML Design
- Primary model: **LightGBM Quantile Regression + Bayesian Change Point**
- Prediction target: `recall_pressure_next_3d`
- Cadence: 15-60 minute intraday scoring windows

## Deliverables
- `src/main.py` orchestration entry point
- Feature pipeline and model API in `src/`
- Alert routing for email/teams/webhooks
- PowerBI push + streaming publisher
- Unit tests under `tests/`
