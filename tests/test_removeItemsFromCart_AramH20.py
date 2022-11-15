from selenium.webdriver.common.by import By


def test_removeItemsFromCart(b):
    expectedResult = 2

    b.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click();
    assert (b.current_url, "https://www.saucedemo.com/cart.html")

    b.find_element(By.ID, "remove-sauce-labs-backpack").click()
    actualResult = b.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").text

    assert (actualResult,expectedResult)