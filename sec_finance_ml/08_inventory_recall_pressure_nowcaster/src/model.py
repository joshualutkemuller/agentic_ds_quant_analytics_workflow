from __future__ import annotations

import numpy as np
import pandas as pd


class ModelService:
    """Simple scoring service stub for production extension."""

    def score(self, features_df: pd.DataFrame) -> pd.DataFrame:
        scores = features_df[["security_id"]].copy()
        scores["risk_score"] = np.clip(features_df["feature_1"] * 0.6 + 0.3, 0, 1)
        return scores
