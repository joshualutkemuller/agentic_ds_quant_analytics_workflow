from __future__ import annotations

import pandas as pd


def generate_alerts(scores_df: pd.DataFrame, warning_threshold: float, critical_threshold: float) -> pd.DataFrame:
    """Label alerts by configured thresholds."""
    alerts = scores_df.copy()
    alerts["alert_level"] = "none"
    alerts.loc[alerts["risk_score"] >= warning_threshold, "alert_level"] = "warning"
    alerts.loc[alerts["risk_score"] >= critical_threshold, "alert_level"] = "critical"
    return alerts
