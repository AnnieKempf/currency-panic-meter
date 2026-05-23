def calculate_panic_level(rate):
    if rate < 5:
        return "calm"
    elif rate < 10:
        return "watch"
    else:
        return "panic"
    
def process_rates(api_data):
    rates = api_data["rates"]

    processed_rated = []

    for currency, rate in rates.items():
        processed_rated.append({
            "currency": currency,
            "rate": rate,
            "panic_level": calculate_panic_level(rate)
        })

    return sorted(processed_rated, key=lambda item: item["rate"], reverse=True)

