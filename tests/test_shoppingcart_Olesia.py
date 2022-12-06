#TC004 Work with shopping cart
import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

Link_mainpage='https://www.saucedemo.com/'
Link_inventory='https://www.saucedemo.com/inventory.html'
Link_cart='https://www.saucedemo.com/cart.html'
Username_valid='standard_user'
Password_valid='secret_sauce'

#Locators
LocatorId_Cart="shopping_cart_container"
# Locator_title_item=(By.XPATH, "//div[@class='inventory_item_name']") #general class for all items
#Locators for Sauce_Labs_Backpack item#4
LocatorId_Item_BTN_remove = 'remove-sauce-labs-backpack'
LocatorId_Item_title='item_4_title_link'
LocatorId_Item_BTN_add = 'add-to-cart-sauce-labs-backpack'
Item_url='https://www.saucedemo.com/inventory-item.html?id=4'
Item_img=(By.XPATH,'//*[@id="item_4_img_link"]/img')

#img in  inventory description
#//*[@id="inventory_item_container"]/div/div/div[1]/img
#<img alt="Sauce Labs Backpack" class="inventory_details_img" src="/static/media/sauce-backpack-1200x1500.34e7aa42.jpg">
#title in inventory description
#<div class="inventory_details_name large_size">Sauce Labs Backpack</div>
#//*[@id="inventory_item_container"]/div/div/div[2]/div[1]
#//*[@class="inventory_details_name large_size"]/text()
#button in inventory description
#//*[@id="remove-sauce-labs-backpack"]
#//*[@id="add-to-cart-sauce-labs-backpack"]
#button back to product
#//*[@id="back-to-products"]
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
        browser.find_element(By.CSS_SELECTOR, locator)
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

backpack_locator = (By.ID, 'remove-sauce-labs-backpack')
backpack_removal = (By.XPATH, "//div[@class='inventory_item_name']")
# cart_quantity = (By.XPATH, "//div[@class='cart_quantity']")
# shopping_cart_bage = (By.XPATH, "//span[@class='shopping_cart_badge']")
inventory_url = 'https://www.saucedemo.com/inventory-item.html?id=4'
#//*[@id="item_4_img_link"]
#//*[@id="item_4_img_link"]/img
shoppingcart_url = 'https://www.saucedemo.com/cart.html'

#TC004.1 Check if the cart button is clickable
def test_cart_button(browser):
    user_login(browser)
    browser.find_element(By.ID, LocatorId_Cart).click()
    assert browser.current_url == Link_cart, 'We are in the cart. Test PASSED'

# TC004.2 Check if the user is able to add the item to the cart
def test_add_items_to_cart(browser):
    browser.find_element(By.ID, LocatorId_Item_BTN_add).click()
    browser.find_element(By.ID, LocatorId_Cart).click()
    assert browser.find_element(By.ID, LocatorId_Item_title), 'Item is in the cart. Test PASSED'



# TC004.3 Check if the user is able to remove the item from the cart
def test_add_items_to_cart(browser):
    browser.find_element(By.ID, LocatorId_Item_BTN_remove).click()
    browser.find_element(By.ID, LocatorId_Cart).click()
    assert browser.find_element(By.ID, 'item_4_title_link'), 'Item is in the cart. Test PASSED'

# # TC005.4 Add the same item multiple times and verify.
# def test_increase_items(d):
#     d.find_element(By.ID, "user-name").send_keys("standard_user")
#     d.find_element(By.ID, "password").send_keys("secret_sauce")
#     d.find_element(By.ID, "login-button").click()
#     d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     shopping_cart_badge = d.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").is_displayed()
#     assert shopping_cart_badge == True
#
# # TC005.7 Click on an item in the cart and verify that the user is redirected to the product detail page.
# def test_product_detail_page(d):
#     d.find_element(By.ID, "user-name").send_keys("standard_user")
#     d.find_element(By.ID, "password").send_keys("secret_sauce")
#     d.find_element(By.ID, "login-button").click()
#     d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     d.find_element(By.ID, "shopping_cart_container").click()
#     d.find_element(By.XPATH, "//div[@class='inventory_item_name']").click()
#     assert inventory_url == 'https://www.saucedemo.com/inventory-item.html?id=4'
#
# # TC004.3 Check if the user is able to remove the item from the shopping cart
# def test_items_removal(d):
#     d.find_element(By.ID, "user-name").send_keys("standard_user")
#     d.find_element(By.ID, "password").send_keys("secret_sauce")
#     d.find_element(By.ID, "login-button").click()
#     d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     d.find_element(By.ID, "shopping_cart_container").click()
#     time.sleep(2)
#     removal_btn = d.find_element(By.ID, "remove-sauce-labs-backpack").is_displayed()
#     assert removal_btn == True
#     time.sleep(2)
#     # cart_is_epmty = d.find_element(By.XPATH, "//div[@class='inventory_item_name']")
#     # assert cart_is_epmty == (By.XPATH, "//div[@class='inventory_item_name']")
#     # time.sleep(2)
#     # assert (By.XPATH, "//div[@class='inventory_item_name']") == backpack_removal
#
# # TC005.8 Check that CONTINUE SHOPPING button works
# def test_continue_shopping_btn(d):
#     d.find_element(By.ID, "user-name").send_keys("standard_user")
#     d.find_element(By.ID, "password").send_keys("secret_sauce")
#     d.find_element(By.ID, "login-button").click()
#     d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     d.find_element(By.ID, "shopping_cart_container").click()
#     d.find_element(By.ID, "continue-shopping").is_displayed()
#     d.find_element(By.ID, "continue-shopping").click()
#     assert inventory_url == 'https://www.saucedemo.com/inventory-item.html?id=4'
#
# # TC005.9 Next step of CHECKOUT the shopping
# def test_chechout_btn(d):
#     d.find_element(By.ID, "user-name").send_keys("standard_user")
#     d.find_element(By.ID, "password").send_keys("secret_sauce")
#     d.find_element(By.ID, "login-button").click()
#     d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     d.find_element(By.ID, "shopping_cart_container").click()
#     d.find_element(By.ID, "checkout").click()
#     title = d.find_element(By.CLASS_NAME, 'title').text
#     assert title == 'CHECKOUT: YOUR INFORMATION'
#
# # TC005.10 Ensure that Checkout Page consists of all the details of the product such as Name, Last Name, Zip/Post Code
# def test_checkout_form(d):
#     d.find_element(By.ID, "user-name").send_keys("standard_user")
#     d.find_element(By.ID, "password").send_keys("secret_sauce")
#     d.find_element(By.ID, "login-button").click()
#     d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     d.find_element(By.ID, "shopping_cart_container").click()
#     d.find_element(By.ID, "checkout").click()
#     time.sleep(2)
#     d.find_element(By.ID, "first-name").send_keys('Maks')
#     time.sleep(2)
#     d.find_element(By.ID, "last-name").send_keys('Plank')
#     time.sleep(2)
#     d.find_element(By.ID, "postal-code").send_keys(91210)
#     d.find_element(By.ID, "continue").click()
#     time.sleep(2)
#     title = d.find_element(By.CLASS_NAME, 'title').text
#     assert title == 'CHECKOUT: OVERVIEW'
#
# # TC005.11 Check the CANCEL button
#
# def test_cancel_btn (d):
#     d.find_element(By.ID, "user-name").send_keys("standard_user")
#     d.find_element(By.ID, "password").send_keys("secret_sauce")
#     d.find_element(By.ID, "login-button").click()
#     d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     d.find_element(By.ID, "shopping_cart_container").click()
#     d.find_element(By.ID, "checkout").click()
#     d.find_element(By.ID, "first-name").send_keys('Maks')
#     d.find_element(By.ID, "last-name").send_keys('Plank')
#     d.find_element(By.ID, "postal-code").send_keys(91210)
#     d.find_element(By.ID, "continue").click()
#     d.find_element(By.ID, 'cancel').click()
#     title_catalog = d.find_element(By.CLASS_NAME, 'title').text
#     assert title_catalog == 'PRODUCTS'
#
# # TC005.12 Check the checkout overview page
#
# def test_checkout_page(d):
#     d.find_element(By.ID, "user-name").send_keys("standard_user")
#     d.find_element(By.ID, "password").send_keys("secret_sauce")
#     d.find_element(By.ID, "login-button").click()
#     d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     d.find_element(By.ID, "shopping_cart_container").click()
#     d.find_element(By.ID, "checkout").click()
#     d.find_element(By.ID, "first-name").send_keys('Maks')
#     d.find_element(By.ID, "last-name").send_keys('Plank')
#     d.find_element(By.ID, "postal-code").send_keys(91210)
#     d.find_element(By.ID, "continue").click()
#     title_payment_info = d.find_element(By.CLASS_NAME, "summary_info_label").text
#     assert title_payment_info == 'Payment Information:'
#     title_shipping_info = d.find_element(By.CLASS_NAME, 'summary_info_label').text
#     assert title_shipping_info == 'Shipping Information:'
#
#
#
#
#
#
#
#

