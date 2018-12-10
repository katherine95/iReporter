import psycopg2
import os

print(os.getenv('APP_SETTINGS'))
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
try:
    conn
except:
    print("I'm unable to connect to database!")
