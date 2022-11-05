
import time
from webbrowser import BaseBrowser
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

driver.get("https://www.saucedemo.com/")

def login_title():
    title_from_site = driver.title #method of selenium webdriver
    assert title_from_site =='Swag Labs', "write site"

def test_login_form():
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    time.sleep(1)

    password = driver.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
    time.sleep(1)

    button_login =driver.find_element(By.XPATH, "//input[@name='login-button']").click()

    time.sleep(1)

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We reached another site!'

    driver.quit()
#hhh