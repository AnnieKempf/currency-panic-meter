import sqlite3
import logging

DATABASE_NAME = "exchange_data.db"

def create_table():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency TEXT NOT NULL,
            rate REAL NOT NULL,
            panic_level TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
        
        connection.commit()

        logging.info("Database table checked/created.")


def save_rates_to_database(data):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.executemany("""
        INSERT INTO exchange_rates (currency, rate, panic_level)
        VALUES (?, ?, ?)
        """, [
            (item["currency"], item["rate"], item["panic_level"])
            for item in data
        ])

        connection.commit()

    logging.info("Exchange rates saved to database.")


def read_rates_from_database():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute("""
        SELECT currency, rate, panic_level, created_at
        FROM exchange_rates
        ORDER BY created_at DESC
        """)

        return cursor.fetchall()
