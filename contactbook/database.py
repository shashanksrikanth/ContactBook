import sqlite3
from sqlite3 import Error
import os
import click


def create_connection(db_file):
    # Create a connection to a SQLite database
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return connection


def create_table(connection, create_table_sql):
    # Create a table using the SQL command passed through as create_table_sql
    try:
        c = connection.cursor()
        c.executescript(create_table_sql)
    except Error as e:
        print(e)


@click.command()
def initialize_database():
    # Initialize a database by creating a connection and creating tables
    current_directory = os.getcwd()
    db_file = current_directory+"/ContactBook/database.db"
    print(db_file)
    user_table = """ DROP TABLE IF EXISTS user;
                    CREATE TABLE user (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    );"""
    contact_table = """ DROP TABLE IF EXISTS contact;
                    CREATE TABLE contact (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES user (id)
                    );"""
    connection = create_connection(db_file)
    if connection is not None:
        create_table(connection, user_table)
        create_table(connection, contact_table)
        click.echo("Tables user and contact have been initialized")
    else:
        click.echo("Error! Cannot create database connection")
