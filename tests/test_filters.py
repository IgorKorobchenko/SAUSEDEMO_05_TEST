import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = False
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
driver.get('https://www.saucedemo.com/')

def test_login_page():
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We are on the product page. Test PASSED'
time.sleep(5)

def test_filter():
    dropdown = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown.click()

time.sleep(5)
