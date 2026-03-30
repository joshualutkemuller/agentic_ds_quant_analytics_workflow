from __future__ import annotations

import pandas as pd


def build_features(raw_df: pd.DataFrame) -> pd.DataFrame:
    """Build model-ready features."""
    features = raw_df.copy()
    features["feature_ratio"] = features["feature_2"] / (features["feature_1"] + 1)
    return features
