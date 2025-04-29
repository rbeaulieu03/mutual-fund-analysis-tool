import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Mutual Fund Analysis Tool", layout="centered")
st.title("💸 Raymond's Mutual Fund Analyzer")
st.write("Enter a mutual fund ticker below to retrieve key metrics and performance trends.")

# --- User Input ---
ticker_input = st.text_input("Mutual Fund Ticker (e.g., VFIAX, SWPPX)", value="VFIAX")

# --- Function to Fetch and Process Data ---
def get_fund_data(ticker):
    try:
        fund = yf.Ticker(ticker)
        hist = fund.history(period="5y")

        if hist.empty:
            return None, None, None, None

        latest_price = hist['Close'].iloc[-1]
        returns = hist['Close'].pct_change().dropna()
        estimated_annual_return = (1 + returns.mean()) ** 252 - 1  # Approximation
        volatility = returns.std() * (252 ** 0.5)

        return latest_price, estimated_annual_return, volatility, hist
    except Exception as e:
        return None, None, None, None

# --- Analysis Button ---
if st.button("Get Analysis"):
    with st.spinner("Fetching data..."):
        latest_price, annual_return, volatility, hist_data = get_fund_data(ticker_input.strip())

    if hist_data is None:
        st.error("Could not retrieve data. Please check the ticker and try again.")
    else:
        # Display Metrics
        st.subheader("Key Performance Metrics:")
        st.metric("Latest Price", f"${latest_price:.2f}")
        st.metric("Estimated Annual Return", f"{annual_return:.2%}")
        st.metric("Risk (Volatility)", f"{volatility:.2%}")

        # Display Line Chart
        st.subheader("Historical Price Trend:")
        fig, ax = plt.subplots()
        ax.plot(hist_data.index, hist_data['Close'], linewidth=2)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price ($)")
        ax.set_title(f"{ticker_input.upper()} Price Trend (Last 5 Years)")
        ax.grid(True)
        st.pyplot(fig)

# --- Footer ---
st.markdown("---")
st.caption("© 2025 Raymond Beaulieu - Mutual Fund Analysis Tool")
