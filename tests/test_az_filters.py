import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.headless = True
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
driver.get('https://www.saucedemo.com/')

def test_login_page():
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We are on the product page. Test PASSED'

time.sleep(2)

def test_dropdown():
    dropdown = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown.click()
    time.sleep(2)
    select = Select(dropdown)
    select.select_by_value('az')

    # dropdown.click()
    time.sleep(2)