# Database functions

import sqlite3
from sqlite3 import Error
import os
import click
from werkzeug.security import check_password_hash

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
    db_file = current_directory+"/contactbook/database.db"
    user_table = """ DROP TABLE IF EXISTS user;
                    CREATE TABLE user (
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    );"""
    contact_table = """ DROP TABLE IF EXISTS contact;
                    CREATE TABLE contact (
                        username TEXT, 
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        FOREIGN KEY (username) REFERENCES user (username)
                    );"""
    connection = create_connection(db_file)
    if connection is not None:
        create_table(connection, user_table)
        create_table(connection, contact_table)
        click.echo("Tables user and contact have been initialized")
    else:
        click.echo("Error! Cannot create database connection")

def check_registration(username):
    # Check if a user is registered in the database
    current_directory = os.getcwd()
    db_file = current_directory+"/contactbook/database.db"
    connection = create_connection(db_file)
    cur = connection.cursor()
    cur.execute("SELECT * FROM user WHERE username=?", (username,))
    if cur.fetchone() is not None: 
        userExists = True
    else:
        userExists = False
    return userExists

def register_user(credentials):
    # Register a user in the database
    current_directory = os.getcwd()
    db_file = current_directory+"/contactbook/database.db"
    connection = create_connection(db_file)
    cur = connection.cursor()
    sql_command = "INSERT INTO user(username, password) VALUES(?,?)"
    cur.execute(sql_command, credentials)
    connection.commit()
    return cur.lastrowid

def check_login(username, password):
    # Check if username and password are correct
    result = []
    current_directory = os.getcwd()
    db_file = current_directory+"/contactbook/database.db"
    connection = create_connection(db_file)
    cur = connection.cursor()
    record = cur.execute("SELECT * FROM user WHERE username=?", (username,)).fetchone()
    if record is None:
        result.append(False)
        result.append("Incorrect username. Have you registered as a user?")
    elif not check_password_hash(record[1], password):
        result.append(False)
        result.append("Incorrect password.")
    else:
        result.append(True)
        result.append("Login successful!")
    return result

def insert_contact(information):
    # Insert a contact into the contact book
    current_directory = os.getcwd()
    db_file = current_directory+"/contactbook/database.db"
    connection = create_connection(db_file)
    cur = connection.cursor()
    sql_command = "INSERT INTO contact(username, name, email, phone) VALUES(?,?,?,?)"
    cur.execute(sql_command, information)
    connection.commit()
    return cur.lastrowid

def get_contact(username, contactname):
    # Get contact information for one person
    current_directory = os.getcwd()
    db_file = current_directory+"/contactbook/database.db"
    connection = create_connection(db_file)
    cur = connection.cursor()
    cur.execute("SELECT * FROM contact WHERE username=? AND name=?",(username,contactname,))
    contacts = cur.fetchall()
    return contacts

def get_all_contacts(username):
    # Get all contacts of a user
    current_directory = os.getcwd()
    db_file = current_directory+"/contactbook/database.db"
    connection = create_connection(db_file)
    cur = connection.cursor()
    cur.execute("SELECT * FROM contact WHERE username=?",(username,))
    contacts = cur.fetchall()
    return contacts