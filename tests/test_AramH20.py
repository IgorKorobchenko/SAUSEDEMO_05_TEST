from selenium.webdriver.common.by import By

def test_CartBox(b):
    expectedResult = 3
    actualResult = b.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").text

    assert (b.current_url == "https://www.saucedemo.com/inventory.html"
    ), "We are on the product page. Test PASSED"
    assert (expectedResult, actualResult) , "wrong number of items"

