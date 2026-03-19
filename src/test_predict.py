from src.predict import predict_risk

# sample input:
# [price_volatility, demand_change, supplier_delay, inventory_level, transport_cost]
test_input = [20, 15, 5, 60, 25]

risk = predict_risk(test_input)

print("Predicted risk level (0=Low,1=Medium,2=High):", risk)
