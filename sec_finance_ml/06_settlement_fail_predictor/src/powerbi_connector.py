from __future__ import annotations

import pandas as pd


def publish_to_powerbi(payload_df: pd.DataFrame) -> None:
    """Placeholder for PowerBI push dataset integration."""
    _ = payload_df.to_dict(orient="records")
