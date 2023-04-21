import threading
import time

from outlook.register import signup, save_account, close_driver, quit_driver
from setup.setup_driver import setup_driver, configure_extension
from util.generator import generate_username, generate_password
from wireguard.connect import start_random_connection, close_connection, force_quit_connection

drivers = []


def create_account():
    try:
        local_driver = setup_driver()
    except Exception as e:
        print(e)
        return
    try:
        drivers.append(local_driver)
        configure_extension(local_driver)
        username = generate_username()
        password = generate_password(10)
        try:
            signup(local_driver, username, password)
        except Exception as e:
            print(e)
            return
        save_account(local_driver, username, password)
    except Exception as e:
        print(e)


while True:
    connection = start_random_connection()

    # Create and start 3 threads to run the create_account_and_close_connection function
    threads = [threading.Thread(target=create_account) for _ in range(3)]

    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join(timeout=80)

    for driver in drivers:
        try:
            close_driver(driver)
        except Exception as e:
            print(e)
            try:
                quit_driver(driver)
            except Exception as e:
                print(e)
    try:
        close_connection(connection)
    except Exception as e:
        print(e)
        force_quit_connection()
