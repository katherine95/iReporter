import psycopg2
import os

url='dbname="ireporter", user="postgres", host="localhost", password="root"'
test_url='dbname="ireporter", user="postgres", host="localhost", password="root"'

conn = psycopg2.connect(
dbname="ireporter",
user="postgres",
host='localhost',
password='root'    
)

try:
    conn
except:
    print("I'm unable to connect to database!")

