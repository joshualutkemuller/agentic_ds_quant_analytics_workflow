from __future__ import annotations

from pathlib import Path

import yaml

from alerts import generate_alerts
from data_ingestion import DataIngestion
from feature_engineering import build_features
from model import ModelService
from powerbi_connector import publish_to_powerbi


def run_pipeline(config_path: str) -> None:
    config = yaml.safe_load(Path(config_path).read_text())

    raw_df = DataIngestion().load()
    features_df = build_features(raw_df)
    scores_df = ModelService().score(features_df)

    thresholds = config["thresholds"]
    alerts_df = generate_alerts(
        scores_df,
        warning_threshold=thresholds["warning"],
        critical_threshold=thresholds["critical"],
    )
    publish_to_powerbi(alerts_df)


if __name__ == "__main__":
    run_pipeline("config/config.yaml")
