import time
from selenium.webdriver.common.by import By

def test_ceckCheckouinformationForm(b):
    first_name = "John"
    last_name = "Smith"
    zip = 15230
    expectedResult = "https://www.saucedemo.com/checkout-step-two.html"
    b.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    b.find_element(By.ID, "checkout").click()
    b.find_element(By.ID, "first-name").send_keys(first_name)
    b.find_element(By.ID, "last-name").send_keys(last_name)
    b.find_element(By.ID, "postal-code").send_keys(zip)

    b.find_element(By.ID, "continue").click()
    assert (b.current_url, expectedResult)