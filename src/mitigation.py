def get_mitigation_strategy(risk_level):
    if risk_level == 2:  # High risk
        return [
            "Diversify suppliers",
            "Increase safety stock",
            "Secure long-term contracts"
        ]
    elif risk_level == 1:  # Medium risk
        return [
            "Monitor demand closely",
            "Optimize inventory levels"
        ]
    else:  # Low risk
        return [
            "Maintain current operations",
            "Periodic risk review"
        ]
