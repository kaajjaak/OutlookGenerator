from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from util.generator import generate_names
import random
from util.files import add_account


def signup(driver, username, password):
    driver.get("https://signup.live.com/signup")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, 'liveSwitch')))
    driver.find_element(By.ID, "liveSwitch").click()

    driver.find_element(By.ID, "MemberName").send_keys(f"{username}")
    driver.find_element(By.ID, "iSignupAction").click()

    wait.until(EC.element_to_be_clickable((By.ID, 'PasswordInput')))
    driver.find_element(By.ID, 'PasswordInput').send_keys(f'{password}')
    driver.find_element(By.ID, "iSignupAction").click()
    first_name, last_name = generate_names()

    wait.until(EC.element_to_be_clickable((By.ID, 'FirstName')))
    driver.find_element(By.ID, 'FirstName').send_keys(f'{first_name}')
    driver.find_element(By.ID, 'LastName').send_keys(f'{last_name}')
    driver.find_element(By.ID, 'iSignupAction').click()

    wait.until(EC.element_to_be_clickable((By.ID, 'BirthMonth'))).click()
    select = Select(driver.find_element(By.ID, 'BirthMonth'))
    select.select_by_value(f"{random.randint(1, 12)}")
    select = Select(driver.find_element(By.ID, 'BirthDay'))
    select.select_by_value(f"{random.randint(1, 27)}")
    driver.find_element(By.ID, 'BirthYear').send_keys(f'{random.randint(1950, 2002)}')
    driver.find_element(By.ID, 'iSignupAction').click()


def save_account(driver, username, password):
    wait = WebDriverWait(driver, 5)
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'wlspispHipControlButtonsContainer')))
    except TimeoutException:
        try:
            wait = WebDriverWait(driver, 30)
            wait.until(EC.presence_of_element_located((By.ID, 'id__0')))
            driver.find_element(By.ID, 'id__0').click()
            wait = WebDriverWait(driver, 3)
            wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
            add_account(f"{username}@outlook.com", password)
        except Exception as e:
            print(e)


def close_driver(driver):
    try:
        driver.close()
    except Exception as e:
        print(e)


def quit_driver(driver):
    driver.quit()
