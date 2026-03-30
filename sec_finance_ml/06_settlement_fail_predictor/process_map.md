# Process Map — 06_settlement_fail_predictor

1. Ingest market + internal lending/borrow data snapshots.
2. Build desk-level and security-level features.
3. Train/load model and score latest universe.
4. Trigger alerts for `Fail risk > threshold; projected fail-notional breach.`
5. Publish scored rows and alert metadata to PowerBI datasets.
6. Log outcomes for model governance and monitoring.
