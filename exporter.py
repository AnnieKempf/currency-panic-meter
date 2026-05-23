import json
import csv
import logging

def export_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    logging.info(f"Exported data to {filename}.")

def export_to_csv(data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["currency", "rate", "panic_level"])
        writer.writeheader()
        writer.writerows(data)

    logging.info(f"Exported data to {filename}")