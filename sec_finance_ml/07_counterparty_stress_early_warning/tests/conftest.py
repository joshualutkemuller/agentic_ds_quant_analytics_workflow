from __future__ import annotations

import pandas as pd
import pytest


@pytest.fixture
def sample_features() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "security_id": ["SEC1", "SEC2"],
            "feature_1": [0.2, 0.8],
            "feature_2": [10, 30],
            "feature_ratio": [8.3, 16.7],
        }
    )
