import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Trading Platform", layout="wide")

st.title("AI Trading Platform")
st.caption("US Equities • EUR/USD • Algorithmic Trading")

# Main navigation
page = st.sidebar.selectbox(
    "Navigation",
    ["Overview", "US Stocks", "EUR/USD", "Algorithms", "Risk Management", "Trade History"]
)

# Account overview
st.subheader("Portfolio Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Portfolio Value", "€19,000", "0.0%")
col2.metric("Total Return", "0.00%", "€0.00")
col3.metric("Open Positions", "0")
col4.metric("Trading Mode", "Paper Trading")

st.divider()

st.subheader(page)

if page == "Overview":
    st.info("Your trading system dashboard is ready for development.")
elif page == "US Stocks":
    st.write("US stock market analysis will go here.")
elif page == "EUR/USD":
    st.write("EUR/USD analysis will go here.")
elif page == "Algorithms":
    st.write("Your mathematical and AI algorithms will go here.")
elif page == "Risk Management":
    st.write("Risk metrics and exposure limits will go here.")
elif page == "Trade History":
    st.write("Simulated and historical trades will go here.")
