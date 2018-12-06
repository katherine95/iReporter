import psycopg2
import os

from app.db_config import conn

def create_tables():
    curr = conn.cursor()
    queries = tables()
    for query in queries:
        curr.execute(query)
    conn.commit()
    print("Users and Incidents tables created!")

def destroy_tables():
    pass

def tables():
    users= """CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        username VARCHAR(20) NOT NULL,
        email VARCHAR(40) NOT NULL,
        date_created timestamp with time zone DEFAULT('now'::text)::date NOT NULL,
        password VARCHAR(50) NOT NULL,
        registered timestamp with time zone DEFAULT('now'::text)::date NOT NULL,
        isAdmin BOOLEAN NOT NULL
    )"""

    incidents = """CREATE TABLE IF NOT EXISTS incidents(
        id serial PRIMARY KEY NOT NULL,
        createdOn timestamp with time zone DEFAULT('now'::text)::date NOT NULL,
        createdBy numeric(50) NOT NULL,
        incidentType VARCHAR(50) NOT NULL,
        location VARCHAR(10) NOT NULL,
        status VARCHAR(10) NOT NULL,
        comment VARCHAR(100) NOT NULL
    )"""

    queries = [users, incidents]
    return queries

create_tables()