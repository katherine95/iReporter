import psycopg2
import os

url='dbname="ireporter", user="postgres", host="localhost", password="root"'
test_url='dbname="ireporter", user="postgres", host="localhost", password="root"'
# url = os.getenv('DB_URL')
# test_url = os.getenv('TEST_DB_URL')

conn = psycopg2.connect(
dbname="test_ireporter",
user="postgres",
host='localhost',
password='root'    
)

try:
    conn
except:
    print("I'm unable to connect to database!")

