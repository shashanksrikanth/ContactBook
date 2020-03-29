# Login to the application and use it
from contactbook import database
import click
from pyfiglet import Figlet

def login(username, password):
    # Check login authentication
    result = database.check_login(username, password)
    if result[0] == False:
        print(result[1])
        return result[0]
    print(result[1])
    return result[0]

def addContact(username):
    # Add a contact for a username
    print("Add a contact. Enter QUIT to exit the program.")
    exit_program = ""
    while(exit_program != "quit"):
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        information = (username, name, email, phone)
        confirmation = database.insert_contact(information)
        if confirmation is not None:
            print("Contact successfully added.")
        else:
            print("Contact not successfully added. Did you add all the information?")
        exit_program = input("Quit Contact Book?: ").lower()
    print("Thank you for using Contact Book!")


@click.command()
@click.option('--username', prompt='Enter username', required=True)
@click.option('--password', prompt='Enter password', required=True, hide_input=True)
def login_add(username, password):
    login_successful = login(username, password)
    if not login_successful:
        return
    f = Figlet(font='big')
    click.echo(f.renderText('Contact Book'))
    addContact(username)

@click.command()
@click.option('--username', prompt='Enter username', required=True)
@click.option('--password', prompt='Enter password', required=True, hide_input=True)
def get_contacts(username, password):
    # Retrieve contacts for username
    login_successful = login(username, password)
    if not login_successful:
        return
    f = Figlet(font='big')
    click.echo(f.renderText('Contact Book'))
    contact_type = input("Type SINGLE for retrieval of contact information for one person. Type ALL for retrieval of all contacts: ").lower()
    if(contact_type == "all"):
        print("You have asked for all contacts. Program will end after outputting your contact list.")
        contacts = database.get_all_contacts(username)
        if(len(contacts)==0):
                print("No contact with the name {} found".format(name))
        else:
            for contact in contacts:
                print("Name: {}".format(contact[1]))
                print("Email: {}".format(contact[2]))
                print("Phone Number: {}".format(contact[3]))
                print("****")
    elif(contact_type == "single"):
        print("Retrieve a single contact. Enter QUIT to exit Contact Book.")
        exit_program = ""
        while(exit_program != "quit"):
            name = input("Enter name: ")
            contacts = database.get_contact(username, name)
            if(len(contacts)==0):
                print("No contact with the name {} found".format(name))
            else:
                for contact in contacts:
                    print("Name: {}".format(contact[1]))
                    print("Email: {}".format(contact[2]))
                    print("Phone Number: {}".format(contact[3]))
                    print("****")
            exit_program = input("Quit Contact Book?: ").lower()
    else:
        print("Not a valid input.")
    print("Thank you for using Contact Book!")