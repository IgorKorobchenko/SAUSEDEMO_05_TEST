from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

o = webdriver.FirefoxOptions()
o.headless = True
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=o)

def test_open_main_page():
    driver.get('https://www.saucedemo.com/')
    assert driver.title == 'Swag Labs'
    driver.quit()