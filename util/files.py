import os
from random import choice


def add_account(email, password):
    filename = 'accounts.txt'

    # Check if the file exists, create it if not
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            pass

    # Open the file in append mode and add the username and password
    with open(filename, 'a') as file:
        file.write(f"{email}:{password}\n")

def random_connection():
    folder_path = r"C:\Users\Jaak\Desktop\NERD\OutlookGenerator\wireguard_configs"

    # Get a list of all the files in the folder
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]

    # Filter out any directories (if any exist)
    files = [f for f in files if os.path.isfile(f)]

    # Get a random file path
    return choice(files)
