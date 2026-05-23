from logger_config import setup_logger
from api_client import fetch_exchange_rates
from processor import process_rates
from exporter import export_to_csv, export_to_json

def main():
    setup_logger()

    base_currency = "SEK"
    target_currencies = ["USD", "EUR", "GBP", "NOK", "DKK", "JPY"]

    api_data = fetch_exchange_rates(base_currency, target_currencies)
    processed_rates = process_rates(api_data)

    for item in processed_rates:
        print(f"{item['currency']}: {item['rate']} - {item['panic_level']}")

    export_to_json(processed_rates, "exchange_rates.json")
    export_to_csv(processed_rates, "exchange_rates.csv")

if __name__ == "__main__":
    main()