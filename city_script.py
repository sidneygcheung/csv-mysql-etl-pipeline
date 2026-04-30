import csv
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

def import_cities(file_path):
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        rows = [
            (row["city_name"], row["state_id"])
            for row in reader
        ]

    sql = """
        INSERT INTO cities (city_name, state_id)
        VALUES (%s, %s)
    """

    cursor.executemany(sql, rows)
    conn.commit()
    print("Cities import completed.")

import_cities("cities.csv")

cursor.close()
conn.close()