import requests


def get_prices_from_deribit():
    result = {}

    indexes = {
        "BTC_USD": "btc_usd",
        "ETH_USD": "eth_usd"
    }

    for ticker, index_name in indexes.items():
        url = f"https://www.deribit.com/api/v2/public/get_index_price?index_name={index_name}"
        response = requests.get(url).json()
        result[ticker] = response["result"]["index_price"]

    return result