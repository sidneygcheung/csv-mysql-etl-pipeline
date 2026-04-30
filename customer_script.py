import csv
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = True
LIMIT = 9000

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

def import_customers(file_path):
    sql = """
        INSERT INTO customers
        (first_name, last_name, address, city_id, state_id, phone_number, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    rows = []

    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader):
            if i >= LIMIT:
                break

            if DEBUG:
                print(f"Processing: {row['first_name']} {row['last_name']}")

            rows.append((
                row["first_name"],
                row["last_name"],
                row["address"],
                row["city_id"],
                row["state_id"],
                row["phone_number"],
                row["email"]
            ))

    cursor.executemany(sql, rows)
    conn.commit()
    print("Customers import completed.")

import_customers("sample_people.csv")

cursor.close()
conn.close()