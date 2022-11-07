from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

o = webdriver.FirefoxOptions()
o.headless = True
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=o)
driver.get('https://www.saucedemo.com/')

def test_login():
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We are on the product page. Test PASSED'

    driver.quit()
