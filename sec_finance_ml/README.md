# SEC Finance ML — Expansion Pack for FSIP

Three additional production-ready ML sub-models for a securities finance desk at State Street. These models follow the same delivery pattern as the existing FSIP projects: self-contained pipelines, alerting, and PowerBI publishing.

---

## Projects

| # | Folder | Description | ML Approach |
|---|--------|-------------|-------------|
| 6 | [`06_settlement_fail_predictor`](./06_settlement_fail_predictor/) | Predict settlement fail probability and inventory lock-up risk across loan returns and recalls. | CatBoost Classifier + SHAP |
| 7 | [`07_counterparty_stress_early_warning`](./07_counterparty_stress_early_warning/) | Detect early stress in borrower counterparties using financing behavior, utilization shifts, and margin patterns. | Temporal Fusion Transformer + Isolation Forest |
| 8 | [`08_inventory_recall_pressure_nowcaster`](./08_inventory_recall_pressure_nowcaster/) | Nowcast near-term inventory recall pressure driven by corporate actions, specials, and demand imbalance. | LightGBM Quantile Regression + Bayesian Change Point |

---

## Shared Delivery Pattern

Each project includes:

1. `requirements.txt` with independent dependencies.
2. `config/config.yaml` with data source, model, threshold, and PowerBI dataset settings.
3. End-to-end Python pipeline in `src/` (`main.py`, ingestion, features, model, alerts, PowerBI connector).
4. Unit tests under `tests/test_model.py`.
5. A `process_map.md` for operating workflow and escalation logic.
6. Optional exploratory notebook in `notebooks/exploration.ipynb`.

---

## Repository Structure

```text
sec_finance_ml/
├── README.md
├── 06_settlement_fail_predictor/
├── 07_counterparty_stress_early_warning/
└── 08_inventory_recall_pressure_nowcaster/
```
