import time
from selenium.webdriver.common.by import By

def test_ceckCheckoutButton(b):
    expectedResult = "https://www.saucedemo.com/checkout-step-one.html"
    b.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    b.find_element(By.ID, "checkout").click()
    assert (b.current_url, expectedResult)