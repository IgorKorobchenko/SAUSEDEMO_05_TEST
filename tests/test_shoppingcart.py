from selenium.webdriver.common.by import By
import time
import logging

backpack_locator = (By.ID, 'remove-sauce-labs-backpack')
backpack_removal = (By.XPATH, "//div[@class='inventory_item_name']")
# cart_quantity = (By.XPATH, "//div[@class='cart_quantity']")
# shopping_cart_bage = (By.XPATH, "//span[@class='shopping_cart_badge']")
inventory_url = 'https://www.saucedemo.com/inventory-item.html?id=4'
shoppingcart_url = 'https://www.saucedemo.com/cart.html'

#TC004.1 Check if the cart button is clickable
def test_cart_button(d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
    d.find_element(By.ID, "shopping_cart_container").click()
    assert(d.current_url == "https://www.saucedemo.com/cart.html")

# TC004.2 Check if the user is able to add the item to the cart
def test_add_items_to_cart(d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
    d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    d.find_element(By.ID, "shopping_cart_container").click()
    assert (By.ID, 'remove-sauce-labs-backpack') == backpack_locator

# TC005.4 Add the same item multiple times and verify.
def test_increase_items(d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
    d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    shopping_cart_badge = d.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").is_displayed()
    assert shopping_cart_badge == True

# TC005.7 Click on an item in the cart and verify that the user is redirected to the product detail page.
def test_product_detail_page(d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
    d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    d.find_element(By.ID, "shopping_cart_container").click()
    d.find_element(By.XPATH, "//div[@class='inventory_item_name']").click()
    assert inventory_url == 'https://www.saucedemo.com/inventory-item.html?id=4'

# TC004.3 Check if the user is able to remove the item from the shopping cart
def test_items_removal(d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
    d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    d.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(2)
    removal_btn = d.find_element(By.ID, "remove-sauce-labs-backpack").is_displayed()
    assert removal_btn == True
    time.sleep(2)
    # cart_is_epmty = d.find_element(By.XPATH, "//div[@class='inventory_item_name']")
    # assert cart_is_epmty == (By.XPATH, "//div[@class='inventory_item_name']")
    # time.sleep(2)
    # assert (By.XPATH, "//div[@class='inventory_item_name']") == backpack_removal

# TC005.8 Check that CONTINUE SHOPPING button works
def test_continue_shopping_btn(d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
    d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    d.find_element(By.ID, "shopping_cart_container").click()
    d.find_element(By.ID, "continue-shopping").is_displayed()
    d.find_element(By.ID, "continue-shopping").click()
    assert inventory_url == 'https://www.saucedemo.com/inventory-item.html?id=4'

# TC005.9 Next step of CHECKOUT the shopping
def test_chechout_btn(d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
    d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    d.find_element(By.ID, "shopping_cart_container").click()
    d.find_element(By.ID, "checkout").click()
    title = d.find_element(By.CLASS_NAME, 'title').text
    assert title == 'CHECKOUT: YOUR INFORMATION'

# TC005.10 Ensure that Checkout Page consists of all the details of the product such as Name, Last Name, Zip/Post Code
def test_checkout_form(d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
    d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    d.find_element(By.ID, "shopping_cart_container").click()
    d.find_element(By.ID, "checkout").click()
    time.sleep(2)
    d.find_element(By.ID, "first-name").send_keys('Maks')
    time.sleep(2)
    d.find_element(By.ID, "last-name").send_keys('Plank')
    time.sleep(2)
    d.find_element(By.ID, "postal-code").send_keys(91210)
    d.find_element(By.ID, "continue").click()
    time.sleep(2)
    title = d.find_element(By.CLASS_NAME, 'title').text
    assert title == 'CHECKOUT: OVERVIEW'

# TC005.11 Check the CANCEL button

def test_cancel_btn (d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
    d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    d.find_element(By.ID, "shopping_cart_container").click()
    d.find_element(By.ID, "checkout").click()
    d.find_element(By.ID, "first-name").send_keys('Maks')
    d.find_element(By.ID, "last-name").send_keys('Plank')
    d.find_element(By.ID, "postal-code").send_keys(91210)
    d.find_element(By.ID, "continue").click()
    d.find_element(By.ID, 'cancel').click()
    title_catalog = d.find_element(By.CLASS_NAME, 'title').text
    assert title_catalog == 'PRODUCTS'

# TC005.12 Check the checkout overview page

def test_checkout_page(d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
    d.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    d.find_element(By.ID, "shopping_cart_container").click()
    d.find_element(By.ID, "checkout").click()
    d.find_element(By.ID, "first-name").send_keys('Maks')
    d.find_element(By.ID, "last-name").send_keys('Plank')
    d.find_element(By.ID, "postal-code").send_keys(91210)
    d.find_element(By.ID, "continue").click()
    title_payment_info = d.find_element(By.CLASS_NAME, "summary_info_label").text
    assert title_payment_info == 'Payment Information:'
    title_shipping_info = d.find_element(By.CLASS_NAME, 'summary_info_label').text
    assert title_shipping_info == 'Shipping Information:'









