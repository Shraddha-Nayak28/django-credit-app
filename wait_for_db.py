import time
import psycopg2
import os

while True:
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
            host="db",
            port="5432",
        )
        conn.close()
        print("PostgreSQL is ready!")
        break
    except psycopg2.OperationalError:
        print("Waiting for PostgreSQL...")
        time.sleep(2)
