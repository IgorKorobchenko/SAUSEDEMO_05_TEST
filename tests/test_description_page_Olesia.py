#TC002 Work with descripton page
import time

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

# Locators for description page
BTN_back_to_product=(By.ID,'back-to-products')

#Locators for item #4 Sauce Labs Backpack
Locator_Cart=(By.ID,"shopping_cart_container")
Locator_Item_BTN_remove = (By.ID,'remove-sauce-labs-backpack')
Locator_Item_title=(By.CSS_SELECTOR,'#item_4_title_link>.inventory_item_name')
Locator_Item_BTN_add = (By.ID,'add-to-cart-sauce-labs-backpack')
Item_url='https://www.saucedemo.com/inventory-item.html?id=4'
Item_img=(By.XPATH,'//*[@id="item_4_img_link"]/img')

@pytest.fixture(scope='module')
def browser():
    o = webdriver.FirefoxOptions()
    o.headless = False
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=o)
    yield driver
    driver.quit()

#Check for presence of element on the screen. If element is not in the screen return True
def element_is_not_present(locator):
    try:
        browser.find_element(locator)
        not_found = False
    except:
        not_found = True

    return not_found

#valid user login to reach inventory page
def user_login(browser):

    browser.get(Link_mainpage)
    browser.find_element(By.ID, 'user-name').send_keys(Username_valid)
    browser.find_element(By.ID, 'password').send_keys(Password_valid)
    browser.find_element(By.ID, 'login-button').click()


# TC002.1 Check if the user go to description of item page by click name of items
def test_go_to_description_title(browser):

    user_login(browser)
    browser.find_element(*Locator_Item_title).click()
    assert browser.current_url==Item_url, 'Successfully go to description page. Test PASSED'

# TC002.2 Check if the user go to description of item page by click image of items
def test_see_description_img(browser):
    browser.get(Link_inventory)
    browser.find_element(*Item_img).click()
    assert browser.current_url == Item_url, 'Successfully go to description page. Test PASSED'

# TC002.4 Check if Images of products is seen on description page
def test_image_description_page(browser):


    example_image = browser.find_elements(By.XPATH, '//img[@class="inventory_details_img"]')

    for image in example_image:
        current_link = image.get_attribute("src")
        r = requests.get(current_link)

        try:
            assert r.status_code == 200
        except AssertionError:
            print(current_link + ' delivered response code of ' + str(r.status_code))

# TC002.5 Check if item price of products is seen on description page
def test_price_description_page(browser):

    price_item= browser.find_element(By.XPATH, '//*[@class ="inventory_details_price"]')
    price=price_item.text
    assert price== "$29.99" and price_item.is_displayed()


# TC002.3 Check if the user is able to return to the inventory page from description page
def test_return_to_inventory_from_description_page(browser):

    browser.find_element(*BTN_back_to_product).click()
    assert browser.current_url == Link_inventory, 'Successfully go to inventory page. Test PASSED'

# TC002.6 Check if the user is able to add the item to the cart from description page
def test_add_items_to_cart_from_description(browser):

    browser.find_element(*Locator_Item_title).click()
    browser.find_element(*Locator_Item_BTN_add).click()
    browser.find_element(*Locator_Cart).click()

    assert browser.find_element(*Locator_Item_title), 'Item is in the cart. Test PASSED'


# TC002.7 Check if the user is able to remove the item from the cart from description page
def test_remove_items_to_cart_from_description(browser):

    browser.find_element(*Locator_Item_title).click()
    browser.find_element(*Locator_Item_BTN_remove).click()
    browser.find_element(*Locator_Cart).click()

    assert element_is_not_present(Locator_Item_title), 'Item remove from the cart. Test PASSED'




