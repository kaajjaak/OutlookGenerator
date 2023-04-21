import threading
from outlook.register import signup, save_and_close
from setup.setup_driver import setup_driver, configure_extension
from util.generator import generate_username, generate_password
from wireguard.connect import start_random_connection, close_connection


def create_account():
    try:
        driver = setup_driver()
        configure_extension(driver)
        username = generate_username()
        password = generate_password(10)
        signup(driver, username, password)
        save_and_close(driver, username, password)
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
    finally:
        return


while True:
    # Establish a connection
    try:
        close_connection(connection)
    except:
        pass
    connection = start_random_connection()

    # Create and start 3 threads to run the create_account_and_close_connection function
    threads = [threading.Thread(target=create_account) for _ in range(3)]

    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join(timeout=80)
