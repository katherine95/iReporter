import psycopg2
import os

if os.getenv('APP_SETTINGS') == "development":
    conn = psycopg2.connect(
        dbname="test",
        user="postgres",
        host='localhost',
        password='root',
        port='5433'
        )
elif os.getenv('APP_SETTINGS') == "testing":
    conn = psycopg2.connect(
        dbname="test_ireporter",
        user="postgres",
        host='localhost',
        password='root',
        port='5433'
        )
else:
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
try:
    conn
except Exception as error:
    print("I'm unable to connect to database!" + str(error))
