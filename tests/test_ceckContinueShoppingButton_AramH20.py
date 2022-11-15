import time

from selenium.webdriver.common.by import By


def test_ceckContinueShoppingButton(b):
    expectedResult = "https://www.saucedemo.com/inventory.html"

    b.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    b.find_element(By.ID, "continue-shopping").click()
    assert (b.current_url, expectedResult)
