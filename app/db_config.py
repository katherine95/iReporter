# import psycopg2

# # url = "dbname = 'iReporter" host='localhost' port='5432' user='cate' password='root'"
# # test_url = "dbname = 'iReporter" host='localhost' port='5432' user='cate' password='root'"


# def connection(connect_url):
#     conn = psycopg2.connect(connect_url)
#     return conn

# def init_db():
#     conn = connection(url)
#     return conn

# def init_db():
#     conn = connection(test_url)
#     return

# def init_test_db():
#     conn = connection(test_url)
#     return conn

# def create_tables():
#     pass

# def destroy_tables():
#     pass
# def tables():
#     users= """CREATE TABLE IF NOT EXISTS users(
#         user_id serial PRIMARY KEY NOT NULL
#         first_name
#         last_name
#         username
#         email
#         date_created
#         password
#     )"""

#     incidents = """CREATE TABLE IF NOT EXISTS users(

#     )"""


# # connection = psycopg2.connect(url)
# # curr = connection.cursor()

# # curr.execute(query)
# # connection.commit()

# # connection.close()

# # #fetch
# # curr.execute("SELECT * FROM test_user")
# # data = cur.fetchall()

# # #fetch one
# # curr.execute("SELECT * FROM test_user WHERE name= 'cate'")
# # data.cur.fetch_one()

# # #insert
# # curr.execute("INSERT INTO test_user(name,email) VALUES")

# # at app/init.py

