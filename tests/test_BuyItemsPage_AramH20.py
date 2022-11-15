from selenium.webdriver.common.by import By


def test_BuyItemsPage(b):
    expectedResult1 = "https://www.saucedemo.com/cart.html"
    expectedResult2 = 3
    b.find_element(By.XPATH, "//div[@id ='shopping_cart_container']/a/span").click()
    actualResult1 = b.current_url
    actualResult2 = b.find_elements(By.XPATH, "//div[@id = 'cart_contents_container']//div[@class = 'cart_item']")

    assert (expectedResult1, actualResult1),  "wrong item information"
    assert (expectedResult2, actualResult2),  "wrong number of items"
