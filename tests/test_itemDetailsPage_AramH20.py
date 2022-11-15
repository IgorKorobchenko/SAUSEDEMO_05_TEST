import time
from selenium.webdriver.common.by import By

def test_itemDetailsPage(b):   #failed
    expectedResult1 = "https://www.saucedemo.com/inventory-item.html?id=4"

    b.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    time.sleep(2)
    b.find_element(By.ID, "item_4_title_link").click()
    time.sleep(2)
    assert (b.current_url, expectedResult1)