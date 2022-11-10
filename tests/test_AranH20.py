import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


def test_CartBox():

    expectedResult = 3
    time.sleep(2)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    time.sleep(2)
    actualResult = driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").text

    assert (
            driver.current_url == "https://www.saucedemo.com/inventory.html"
    ), "We are on the product page. Test PASSED"

    assert (expectedResult, actualResult) , "wrong number of items"
    # assert driver.title == "Swag Labs"

    driver.quit()


def test_BuyItemsPage():

    expectedResult1 = "https://www.saucedemo.com/cart.html"
    expectedResult2 = 3
    time.sleep(2)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    actualResult1 = driver.current_url

    actualResult2 = driver.find_elements(By.XPATH, "//div[@id = 'cart_contents_container']//div[@class = 'cart_item']")

    assert (expectedResult1, actualResult1),  "wrong item information"

    assert (expectedResult2, actualResult2),  "wrong number of items"
    driver.quit()


def test_itemDetailsPage():
    expectedResult1 = "https://www.saucedemo.com/inventory-item.html?id=4"
    expectedResult2 = 2

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)

    driver.find_element(By.ID, "item_4_title_link").click()
    assert (driver.current_url, expectedResult1)
    driver.quit()


def test_removeItemsFromCart():
    expectedResult2 = 2

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)

    driver.find_element(By.ID, "item_4_title_link").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    actualResult2 = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/a/span").text

    assert (actualResult2, expectedResult2)

    driver.quit()


def test_ceckContinueShoppingButton():
    expectedResult = "https://www.saucedemo.com/inventory.html"
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "continue-shopping").click()

    assert (driver.current_url, expectedResult)
    driver.quit()

def test_ceckCheckoutButton():
    expectedResult = "https://www.saucedemo.com/checkout-step-one.html"
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "checkout").click()

    assert (driver.current_url, expectedResult)
    driver.quit()


def test_ceckCheckouinformationForm():
    first_name = "John"
    last_name = "Smith"
    zip = 15230
    expectedResult = "https://www.saucedemo.com/checkout-step-two.html"
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(zip)

    driver.find_element(By.ID, "continue").click()

    assert (driver.current_url, expectedResult)
    driver.quit()