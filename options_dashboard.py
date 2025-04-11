
import streamlit as st
import numpy as np
from scipy.stats import norm

st.title("Mini Options Greek Calculator")

# User inputs
S = st.number_input("Spot Price (S)", value=100.0)
K = st.number_input("Strike Price (K)", value=100.0)
T = st.number_input("Time to Expiry (in years)", value=0.5)
r = st.number_input("Risk-Free Rate (r)", value=0.01)
sigma = st.number_input("Implied Volatility (σ)", value=0.2)

# Calculations
def calc_d1_d2(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return d1, d2

d1, d2 = calc_d1_d2(S, K, T, r, sigma)

call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

delta_call = norm.cdf(d1)
delta_put = norm.cdf(d1) - 1
gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
vega = S * norm.pdf(d1) * np.sqrt(T)
theta_call = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2))
theta_put = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2))

# Display results
st.subheader("Option Prices")
st.write(f"Call Price: {call_price:.2f}")
st.write(f"Put Price: {put_price:.2f}")

st.subheader("Greeks")
st.write(f"Delta (Call): {delta_call:.4f}")
st.write(f"Delta (Put): {delta_put:.4f}")
st.write(f"Gamma: {gamma:.4f}")
st.write(f"Vega: {vega:.4f}")
st.write(f"Theta (Call): {theta_call:.4f}")
st.write(f"Theta (Put): {theta_put:.4f}")
