from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
import os
import time


load_dotenv()

# Create a custom Chrome options object
options = Options()

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("disable-blink-features=AutomationControlled")

extension_path = r"./NopeCHA-CAPTCHA-Solver.crx"  # Replace with the correct path to your extension's CRX file
options.add_extension(extension_path)

extension_path_2 = r"./mullvad.crx"  # Replace with the correct path to your extension's CRX file
options.add_extension(extension_path_2)

# Create the Chrome WebDriver with the specified profile
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())


def setup_driver():
    return webdriver.Chrome(service=chrome_service, options=options)


def configure_extension(driver):
    time.sleep(3)
    driver.get(os.environ.get('NOPECHA_URL'))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
