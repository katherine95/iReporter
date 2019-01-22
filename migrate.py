import psycopg2
import os
from passlib.hash import sha256_crypt

from app.db_config import conn
curr = conn.cursor()

password = sha256_crypt.hash("Cate@95#")


def create_tables():
    queries = tables()
    for query in queries:
        curr.execute(query)

    curr.execute("INSERT INTO users( firstname, lastname, othernames,\
        email, phonenumber, username, password, isAdmin)\
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                 ("cate", "chep", "kimetto", "root@gmail.com", "0725277948",
                  "catechep", password, True))
    curr.execute("SELECT * FROM users")
    conn.commit()

    print("Users and Incidents tables created!")


def destroy_tables():
    pass


def tables():
    drop_users = """DROP TABLE IF EXISTS users"""
    drop_incidents = """DROP TABLE IF EXISTS incidents"""
    users = """CREATE TABLE users(
        user_id serial PRIMARY KEY NOT NULL,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        othernames VARCHAR(50) NULL,
        username VARCHAR(20) NOT NULL,
        email VARCHAR(40) NOT NULL,
        phonenumber VARCHAR(40) NOT NULL,
        date_created timestamp with time zone DEFAULT('now'::text)::date
        NOT NULL,
        password VARCHAR NOT NULL,
        registered timestamp with time zone DEFAULT('now'::text)::date
        NOT NULL,
        isAdmin BOOLEAN NOT NULL
    )"""

    incidents = """CREATE TABLE incidents(
        id serial PRIMARY KEY NOT NULL,
        createdOn timestamp with time zone DEFAULT('now'::text)::date NOT NULL,
        createdBy int NOT NULL,
        incidentType VARCHAR(50) NOT NULL,
        location VARCHAR(10) NOT NULL,
        status VARCHAR(10) NOT NULL,
        comment VARCHAR(100) NOT NULL,
        image VARCHAR(300)[] NULL
    )"""

    queries = [drop_users, drop_incidents, users, incidents]
    return queries

create_tables()
