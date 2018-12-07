import psycopg2
import os

url='dbname="ireporter", user="postgres", host="localhost", password="root"'
test_url='dbname="ireporter", user="postgres", host="localhost", password="root"'
if os.getenv('APP_SETTINGS') == "development":
    conn = psycopg2.connect(
    dbname="ireporter",
    user="postgres",
    host='localhost',
    password='root'    
    )
elif os.getenv('APP_SETTINGS') == "testing":
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