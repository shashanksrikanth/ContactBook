# Registering a user
from werkzeug.security import generate_password_hash
import click
import sqlite3
from sqlite3 import Error
import os
from contactbook import database

@click.command()
@click.option('--username', prompt='Enter username', required=True)
@click.option('--password', prompt='Enter password', required=True, hide_input=True, confirmation_prompt=True)
def register_user(username, password):
    if database.check_registration(username) is True:
        click.echo("User is already registered")
    else:
        credentials = (username, generate_password_hash(password))
        confirmation = database.register_user(credentials)
        if confirmation is not None:
            click.echo("User successfully registered!")
        else:
            click.echo("Error in registering user")