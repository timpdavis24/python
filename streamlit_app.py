import streamlit as st
import pandas as pd
import numpy as np

st.title("Fyers Backtesting App")

st.write("App is deployed successfully 🎉")

symbol = st.text_input("Symbol", "NSE:NIFTY50-INDEX")

if st.button("Run Test"):
    data = pd.DataFrame({
        "Price": np.random.randn(100).cumsum()
    })
    st.line_chart(data)
