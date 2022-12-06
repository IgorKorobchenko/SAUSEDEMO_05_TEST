#TC010 Work with inventory page

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

Link_mainpage='https://www.saucedemo.com/'
Link_inventory='https://www.saucedemo.com/inventory.html'
Link_cart='https://www.saucedemo.com/cart.html'

Username_valid='standard_user'
Password_valid='secret_sauce'

@pytest.fixture(scope='module')
def browser():
    o = webdriver.FirefoxOptions()
    o.headless = True
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=o)
    yield driver
    driver.quit()


#valid user login to reach inventory page
def user_login(browser):

    browser.get(Link_mainpage)
    browser.find_element(By.ID, 'user-name').send_keys(Username_valid)
    browser.find_element(By.ID, 'password').send_keys(Password_valid)
    browser.find_element(By.ID, 'login-button').click()

# TC010.1 Check if Images of products is seen in inventory page
def test_images_for_200_response(browser):

    user_login(browser)
    list_error=[]
    example_images = browser.find_elements(By.XPATH, '//img[@class="inventory_item_img"]')

    for image in example_images:
        current_link = image.get_attribute("src")
        r = requests.get(current_link)
        try:
            assert r.status_code == 200
        except AssertionError:
            list_error.append(current_link + ' delivered response code of ' + str(r.status_code))
        assert list_error == []