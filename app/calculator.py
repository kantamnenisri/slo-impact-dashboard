from typing import Dict, Union

def calculate_slo_metrics(
    service_name: str,
    slo_target: float,
    current_uptime: float,
    monthly_revenue: float,
    monthly_traffic: int
) -> Dict[str, Union[str, float]]:
    # Constants
    DAYS_IN_MONTH = 30
    MINUTES_IN_MONTH = DAYS_IN_MONTH * 24 * 60
    HOURS_IN_MONTH = DAYS_IN_MONTH * 24

    # SLO calculations
    max_downtime_mins = MINUTES_IN_MONTH * (1 - slo_target / 100)
    current_downtime_mins = MINUTES_IN_MONTH * (1 - current_uptime / 100)
    
    error_budget_remaining_mins = max_downtime_mins - current_downtime_mins
    
    # Burn rate: how fast we are consuming the budget relative to the allowed rate
    # Burn Rate = (1 - Current Uptime) / (1 - SLO Target)
    if (100 - slo_target) > 0:
        burn_rate = (100 - current_uptime) / (100 - slo_target)
    else:
        burn_rate = 0.0

    # Business impact
    downtime_cost_per_hour = monthly_revenue / HOURS_IN_MONTH
    current_downtime_hours = current_downtime_mins / 60
    revenue_at_risk = current_downtime_hours * downtime_cost_per_hour

    # Health status
    if current_uptime < slo_target:
        status = "BREACHED"
    elif burn_rate > 1.0:
        status = "AT RISK"
    else:
        status = "HEALTHY"

    return {
        "service_name": service_name,
        "slo_target": slo_target,
        "current_uptime": current_uptime,
        "error_budget_remaining_mins": round(error_budget_remaining_mins, 2),
        "burn_rate": round(burn_rate, 2),
        "revenue_at_risk": round(revenue_at_risk, 2),
        "downtime_cost_per_hour": round(downtime_cost_per_hour, 2),
        "status": status
    }
