"""
YTD Utilities Module

This module standardizes Year-to-Date (YTD) inputs
into normalized risk indicators used by the prediction engine.
"""

def normalize_ytd_inputs(
    price_volatility_ytd,
    demand_change_ytd,
    supplier_delay_days,
    inventory_level_ytd,
    transport_cost_ytd
):
    """
    Converts raw YTD inputs into normalized risk-ready values.
    """

    # Price volatility (% YTD)
    price_risk = min(price_volatility_ytd / 50, 1.0)

    # Demand change (% YTD)
    demand_risk = min(abs(demand_change_ytd) / 40, 1.0)

    # Supplier delay (days)
    delay_risk = min(supplier_delay_days / 15, 1.0)

    # Inventory level (% YTD) – inverse risk
    inventory_risk = 1 - min(inventory_level_ytd / 100, 1.0)

    # Transport cost increase (% YTD)
    transport_risk = min(transport_cost_ytd / 50, 1.0)

    return [
        price_risk,
        demand_risk,
        delay_risk,
        inventory_risk,
        transport_risk
    ]
