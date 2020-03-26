# ContactBook
This is a command-line application imitating the functionality of a contact book. It provides authentication, adding contacts, updating contacts, deleting contacts, and providing an option for backups to the user's local machine.

## Technologies used
This list will be updated as the application grows in complexity. 
1. Python
2. Sqlite (for databases)
3. Click (for creating command-line interface applications)
4. Werkzeug (for password authentication, such as generating hashes for passwords)

## Testing of commands
If you have a function you want to make into a command that can be called from the command line (e.g., `ls` and `pwd` are famous ones), add the setup configurations to `setup.py` (follow the structure of the other configuration blocks). Do not move `setup.py` to any other subfolder or such. From `ContactBook`, run `python setup.py develop` (since we are testing it, we are saying it is in develop). After this, you should be able to run your command. For instance, if your command is **mycommand**, you can call it as **mycommand** from the command line. For more options on configuring your function, check out Click's documentation.

## Contribution
To contribute to the project, clone the repository using `git clone ...`. Please do not merge directly to the master branch- create a pull request (PR) form your personal branch and it will be merged upon subsequent testing. Please update any corresponding sections in the README file as well (e.g., if a new technology is used, please add it to the list of technologies used in the project). 

## Documentation Links
1. Sqlite: https://docs.python.org/2/library/sqlite3.html
I used this following link more, even though it does have a few missing commands (such as `connection.commit()` after `INSERT` or `UPDATE` statements): https://www.sqlitetutorial.net/sqlite-python/
2. Click: https://click.palletsprojects.com/en/7.x/