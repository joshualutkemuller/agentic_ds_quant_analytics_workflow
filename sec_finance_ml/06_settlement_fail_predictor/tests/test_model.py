from __future__ import annotations

from src.model import ModelService


def test_model_scores_in_unit_interval(sample_features):
    scores = ModelService().score(sample_features)
    assert scores["risk_score"].between(0, 1).all()
