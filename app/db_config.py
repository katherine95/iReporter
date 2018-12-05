import psycopg2

url = "dbname = 'iReporter" host='localhost' port='5432' user='postgres' password='root'"
test_url = "dbname = 'test_iReporter" host='localhost' port='5432' user='postgres' password='root'"


def connection(connect_url):
    conn = psycopg2.connect(url)
    return conn

def init_db():
    conn = connection(url)
    return

# def init_test_db():
#     conn = connection(test_url)
#     return conn

def create_tables():
    pass

def destroy_tables():
    pass

def tables():
    users= """CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        username VARCHAR(20) NOT NULL,
        email VARCHAR(40) NOT NULL,
        date_created VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        registered VARCHAR(50) NOT NULL,
        isAdmin BOOLEAN NOT NULL
    )"""

    incidents = """CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY NOT NULL,
        createdOn VARCHAR(50) NOT NULL,
        createdBy VARCHAR(50) NOT NULL,
        incidentType VARCHAR(50) NOT NULL,
        location INT(10) NOT NULL,
        status STRING(10) NOT NULL,
        comment VARCHAR(100) NOT NULL
    )"""


