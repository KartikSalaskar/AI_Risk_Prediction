import streamlit as st
from src.predict import predict_risk
from src.mitigation import get_mitigation_strategy

st.set_page_config(
    page_title="AI Risk Prediction Tool (YTD)",
    layout="wide"
)

st.title("📊 AI-Assisted Risk Prediction System")
st.caption("Year-to-Date (YTD) Risk Assessment for Market and Supply Chain")

st.markdown("---")

st.subheader("🔧 Enter YTD Parameters")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📈 Market Indicators (YTD)")
    price_volatility = st.slider(
        "Price Volatility (%) – YTD", 0, 100, 20
    )
    demand_change = st.slider(
        "Demand Change (%) – YTD", -100, 100, 15
    )

with col2:
    st.markdown("### 🚚 Supply Chain Indicators (YTD)")
    supplier_delay = st.slider(
        "Supplier Delay (days)", 0, 30, 5
    )
    inventory_level = st.slider(
        "Inventory Level (%) – YTD", 0, 100, 60
    )
    transport_cost = st.slider(
        "Transport Cost Increase (%) – YTD", 0, 100, 30
    )

st.markdown("---")

if st.button("🚀 Assess YTD Risk", use_container_width=True):

    risk = predict_risk([
        price_volatility,
        demand_change,
        supplier_delay,
        inventory_level,
        transport_cost
    ])

    labels = ["Low", "Medium", "High"]
    icons = ["🟢", "🟡", "🔴"]
    colors = ["green", "orange", "red"]

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:10px;
            border-left:8px solid {colors[risk]};
            background-color:#111;
        ">
        <h2>{icons[risk]} {labels[risk].upper()} RISK (YTD)</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🛡️ Recommended Mitigation Strategies")
    for strategy in get_mitigation_strategy(risk):
        st.write("✔️", strategy)
