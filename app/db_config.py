import psycopg2
import os

url = os.getenv('DB_URL')
test_url = os.getenv('TEST_DB_URL')

try:
    conn = psycopg2.connect(url)
except:
    print("I'm unable to connect to database!")

