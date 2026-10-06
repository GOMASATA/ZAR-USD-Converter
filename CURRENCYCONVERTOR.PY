import requests

API_KEY = "TMSMBFPCI3CUYEND"
BASE_URL = "https://www.alphavantage.co/query"

def get_exchange_rate():
    """
    Fetches the latest ZAR/USD exchange rate from Alpha Vantage.
    """
    params = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "ZAR",
        "to_currency": "USD",
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    # Extract the exchange rate
    rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    return rate

def zar_to_usd(amount_zar):
    rate = get_exchange_rate()
    return amount_zar * rate

def usd_to_zar(amount_usd):
    rate = get_exchange_rate()
    return amount_usd / rate

# Example usage:
zar_amount = 1000
usd_amount = 50

print(f"{zar_amount} ZAR = {zar_to_usd(zar_amount):.2f} USD")
print(f"{usd_amount} USD = {usd_to_zar(usd_amount):.2f} ZAR")
