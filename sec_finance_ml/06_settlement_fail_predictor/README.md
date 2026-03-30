# 06 Settlement Fail Predictor

## Objective
Predict settlement fail probability and inventory lock-up risk across loan returns and recalls.

## ML Design
- Primary model: **CatBoost Classifier + SHAP**
- Prediction target: `t_plus_2_fail_flag`
- Cadence: 15-60 minute intraday scoring windows

## Deliverables
- `src/main.py` orchestration entry point
- Feature pipeline and model API in `src/`
- Alert routing for email/teams/webhooks
- PowerBI push + streaming publisher
- Unit tests under `tests/`
