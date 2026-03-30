from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass
class DataIngestion:
    """Load source data for model scoring."""

    source_name: str = "synthetic"

    def load(self) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "security_id": ["SEC1", "SEC2", "SEC3"],
                "feature_1": [0.1, 0.5, 0.9],
                "feature_2": [10, 20, 30],
            }
        )
