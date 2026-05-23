import requests
import logging

BASE_URL = "https://api.frankfurter.dev/v1/latest"

def fetch_exchange_rates(base_currency, target_currencies):
    params = {
        "base": base_currency,
        "symbols": ",".join(target_currencies)
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        logging.info("Successfully fetched exchange rates.")
        return response.json()
    
    except requests.exceptions.RequestException as error:
        logging.error(f"API request failed: {error}.")
        raise