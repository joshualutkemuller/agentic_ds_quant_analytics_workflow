# Process Map — 08_inventory_recall_pressure_nowcaster

1. Ingest market + internal lending/borrow data snapshots.
2. Build desk-level and security-level features.
3. Train/load model and score latest universe.
4. Trigger alerts for `Recall pressure percentile and expected forced-buyin risk.`
5. Publish scored rows and alert metadata to PowerBI datasets.
6. Log outcomes for model governance and monitoring.
