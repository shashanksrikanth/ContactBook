# Login to the application and use it
from contactbook import database
import click

def login(username, password):
    result = database.check_login(username, password)
    if result[0] == False:
        print(result[1])
        return result[0]
    print(result[1])
    return result[0]

@click.command()
@click.option('--username', prompt='Enter username', required=True)
@click.option('--password', prompt='Enter password', required=True, hide_input=True)
def run_commands(username, password):
    login(username, password)