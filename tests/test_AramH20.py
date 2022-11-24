import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")

@pytest.fixture(autouse=True, scope="module")
def g():
    driver.get('https://www.saucedemo.com/')  # conf.URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    time.sleep(2)
    yield
    driver.quit()


def test_CartBox():
    expectedResult = 3
    actualResult = int(driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").text)
    assert (expectedResult == actualResult), "wrong number of items"
    assert (driver.current_url == "https://www.saucedemo.com/inventory.html"), "We are on the product page. Test PASSED"

def test_BuyItemsPage():
    expectedResult1 = "https://www.saucedemo.com/cart.html"
    expectedResult2 = 3
    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    actualResult1 = driver.current_url
    actualResult2 = driver.find_elements(By.XPATH, "//div[@id = 'cart_contents_container']//div[@class = 'cart_item']")

    assert (expectedResult1 == actualResult1), "wrong item information"
    assert (expectedResult2 == len(actualResult2)), "wrong number of items"

def test_itemDetailsPage():
    expectedResult1 = "https://www.saucedemo.com/inventory-item.html?id=4"
    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "item_4_title_link").click()
    assert (driver.current_url == expectedResult1)


def test_removeItemsFromCart():
    expectedResult = 2
    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "item_4_title_link").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    actualResult = int(driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").text)
    assert (actualResult == expectedResult)


def test_checkContinueShoppingButton():
    expectedResult = "https://www.saucedemo.com/inventory.html"
    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "continue-shopping").click()
    assert (driver.current_url == expectedResult)
    # driver.quit()


def test_checkCheckoutButton():
    expectedResult = "https://www.saucedemo.com/checkout-step-one.html"
    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "checkout").click()
    assert (driver.current_url == expectedResult)


def test_checkCheckoutInformationForm():
    first_name = "John"
    last_name = "Smith"
    zip = 15230
    expectedResult = "https://www.saucedemo.com/checkout-step-two.html"
    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(zip)
    driver.find_element(By.ID, "continue").click()
    actualResult = driver.current_url
    assert (actualResult == expectedResult)


def test_checkoutInfoIncomplitFirstNameForm():
    expectedResult = "Error: First Name is required"
    last_name = "Smith"
    zip = 15230
    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(zip)
    driver.find_element(By.ID, "continue").click()
    actualResult = driver.find_element(By.XPATH, "//div[@id='checkout_info_container']/div/form/div[1]/div[4]/h3").text
    assert (expectedResult == actualResult)


def test_checkoutInfoIncomplitLastNameForm():
    expectedResult = "Error: Last Name is required"
    first_name = "John"
    zip = 15230
    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "postal-code").send_keys(zip)
    driver.find_element(By.ID, "continue").click()
    actualResult = driver.find_element(By.XPATH, "//div[@id='checkout_info_container']/div/form/div[1]/div[4]/h3").text
    print(actualResult)
    assert (expectedResult == actualResult)


def test_checkoutInfoIncomplitZIPForm():
    expectedResult = "Error: Postal Code is required"
    first_name = "John"
    last_name = "Smith"
    driver.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "continue").click()
    actualResult = driver.find_element(By.XPATH, "//div[@id='checkout_info_container']/div/form/div[1]/div[4]/h3").text
    assert (expectedResult == actualResult)

