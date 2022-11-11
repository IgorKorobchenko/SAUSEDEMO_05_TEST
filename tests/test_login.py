#TC001.1 Login with correct username /pasword
#Expected result User should be directed to the page https://www.saucedemo.com/inventory.html
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

o = webdriver.FirefoxOptions()
o.headless = True
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=o)
driver.get('https://www.saucedemo.com/')

def test_login_page():

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We are on the product page. Test PASSED'

    driver.quit()

def test_filter_button ():
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    driver.find_element(By.CLASS_NAME, 'product_sort_container').click()
    DropdownElement=driver.find_element(By.CLASS_NAME,'product_sort_container')
    # verify the dropdown is enabled & visible
    assert (DropdownElement.is_enabled()&DropdownElement.is_displayed()) , "User can open dropdodown filter options"
    driver.quit()

def user_login():
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
#TC003.1
def test_filter_button_open_options():
    user_login()
    FilterSelector=driver.find_element(By.CLASS_NAME,'product_sort_container')
    FilterSelector.click()
    # verify the dropdown is enabled & visible
    assert (FilterSelector.is_enabled()&FilterSelector.is_displayed()) , "User can open dropdown filter options"
    driver.quit()

    # driver.quit()
#TC003.3
# def test_filter_button_choose_options():
#     user_login()
#     FilterSelector = driver.find_element(By.CLASS_NAME, 'product_sort_container')
#     FilterSelector.click()
#     FilterAZ = driver.find_element(By.XPATH, '//option[@value="az"]')
#     FilterAZ.click()
#     # verify the dropdown is enabled & visible
#     assert (DropdownElement.is_enabled()&DropdownElement.is_displayed()) , "User can open dropdodown filter options"
#
#     driver.quit()

#TC004.1 Check if the cart button is clickable
def test_cart_btn():
    user_login()
    driver.find_element(By.ID, 'shopping_cart_container').click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html', 'We are in the cart. Test PASSED'

#TC004.2 Check if the user is able to add the item to the cart
def test_add_item_in_cart():
    user_login()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'shopping_cart_container').click()

    assert driver.find_element(By.ID, 'item_4_title_link'), 'Item is in the cart. Test PASSED'
    driver.quit()
