# Currency Panic Meter

A Python API project that fetches live exchange-rate data, processes currencies into custom "panic levels", and exports the results to JSON and CSV files.

## Features

- Fetches live exchange-rate data from an external API
- Parses JSON API responses
- Processes and sorts currency data
- Assigns custom panic-level categories
- Exports results to JSON and CSV
- Includes logging and error handling
- Uses modular project structure

## Technologies used

- Python
- requests
- JSON
- CSV
- logging

## Project Structure

```text
currency-panic-meter/
│
├── main.py
├── api_client.py
├── processor.py
├── exporter.py
├── logger_config.py
├── requirements.txt
└── README.md
```

## Example Output

```text
JPY: 16.97 - panic
NOK: 0.98 - calm
USD: 0.10 - calm
```

## Installation

Clone the repository:

```bash
git clone https://github.com/AnnieKempf/currency-panic-meter.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## What I Learned

This project helped me practice:
- Working with REST APIs
- Sending HTTP requests with Python
- Parsing JSON responses
- Error handling and logging
- Modular project structure
- Exporting structured data to CSV and JSON
- Debugging API and file-export issues

## Future Improvements

- Add historical exchange-rate comparisons
- Calculate panic levels based on percentage changes
- Add charts/data visualization
- Add unit tests
- Add a small frontend or dashboard