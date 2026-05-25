from logger_config import setup_logger
from api_client import fetch_exchange_rates
from processor import process_rates
from exporter import export_to_csv, export_to_json
from database import create_table, read_rates_from_database, save_rates_to_database

def main():
    setup_logger()

    base_currency = "SEK"
    target_currencies = ["USD", "EUR", "GBP", "NOK", "DKK", "JPY"]

    api_data = fetch_exchange_rates(base_currency, target_currencies)
    processed_rates = process_rates(api_data)

    create_table()
    save_rates_to_database(processed_rates)

    for item in processed_rates:
        print(f"{item['currency']}: {item['rate']} - {item['panic_level']}")

    export_to_json(processed_rates, "exchange_rates.json")
    export_to_csv(processed_rates, "exchange_rates.csv")

    database_rows = read_rates_from_database()

    print("\nLatest database rows:")
    for row in database_rows[:10]:
        print(row)

if __name__ == "__main__":
    main()