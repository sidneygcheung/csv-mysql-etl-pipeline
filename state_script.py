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

def import_states(file_path):
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        rows = [
            (row["state_name"], row["state_code"])
            for row in reader
        ]

    sql = """
        INSERT INTO states (state_name, state_code)
        VALUES (%s, %s)
    """

    cursor.executemany(sql, rows)
    conn.commit()
    print("States import completed.")

import_states("states.csv")

cursor.close()
conn.close()