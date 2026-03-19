from src.ytd_utils import normalize_ytd_inputs

def predict_risk(input_data):
    """
    Predicts risk level using YTD-normalized indicators.
    """

    (
        price_volatility,
        demand_change,
        supplier_delay,
        inventory_level,
        transport_cost
    ) = input_data

    # Normalize YTD inputs
    (
        price_risk,
        demand_risk,
        delay_risk,
        inventory_risk,
        transport_risk
    ) = normalize_ytd_inputs(
        price_volatility,
        demand_change,
        supplier_delay,
        inventory_level,
        transport_cost
    )

    # Risk scoring logic
    risk_score = (
        2 * price_risk +
        2 * demand_risk +
        2 * delay_risk +
        2 * inventory_risk +
        2 * transport_risk
    )

    # Risk classification
    if risk_score >= 7:
        return 2  # High
    elif risk_score >= 4:
        return 1  # Medium
    else:
        return 0  # Low
