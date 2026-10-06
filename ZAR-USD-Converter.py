import streamlit as st
import requests

API_KEY = "TMSMBFPCI3CUYEND"
BASE_URL = "https://www.alphavantage.co/query"

def get_exchange_rate():
    params = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "ZAR",
        "to_currency": "USD",
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    return rate

st.title("💱 ZAR ↔ USD Currency Converter")

rate = get_exchange_rate()
st.write(f"Current Exchange Rate: 1 ZAR = {rate:.4f} USD")

option = st.radio("Choose conversion direction:", ("ZAR → USD", "USD → ZAR"))
amount = st.number_input("Enter amount:", min_value=0.0, format="%.2f")

if st.button("Convert"):
    if option == "ZAR → USD":
        result = amount * rate
        st.success(f"{amount:.2f} ZAR = {result:.2f} USD")
    else:
        result = amount / rate
        st.success(f"{amount:.2f} USD = {result:.2f} ZAR")
