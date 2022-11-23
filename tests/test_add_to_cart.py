import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


link='https://www.saucedemo.com/'

@pytest.fixture(scope='function')
def browser():
    o = webdriver.FirefoxOptions()
    o.headless = False
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=o)
    # return driver
    yield driver
    driver.quit()

# @pytest.fixture(scope='function')
def user_login(browser):

    browser.get(link)
    browser.find_element(By.ID, 'user-name').send_keys('standard_user')
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()


def test_cart_btn(browser):
    """  TC004.1 Check if the cart button is clickable  """
    user_login(browser)
    browser.find_element(By.ID, 'shopping_cart_container').click()

    assert browser.current_url == "https://www.saucedemo.com/cart.html", 'We are in the cart. Test PASSED'


def test_add_item_in_cart(browser):
    """
    TC004.2 Check if the user is able to add the item to the cart
    """
    user_login(browser)
    browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    browser.find_element(By.ID, 'shopping_cart_container').click()

    assert browser.find_element(By.ID, 'item_4_title_link'), 'Item is in the cart. Test PASSED'

