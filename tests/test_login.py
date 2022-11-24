#TC001.1 Login with correct username /pasword
#Expected result User should be directed to the page https://www.saucedemo.com/inventory.html
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#
# o = webdriver.ChromeOptions()
# o.headless = True
# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()), options=o
# )
# driver.get("https://www.saucedemo.com/")


def test_login_page(b):
    # b.find_element(By.ID, "user-name").send_keys("standard_user")
    # b.find_element(By.ID, "password").send_keys("secret_sauce")
    # b.find_element(By.ID, "login-button").click()
    assert (
        b.current_url == "https://www.saucedemo.com/inventory.html"
    ), "We are on the product page. Test PASSED"

    b.quit()
#Hello
#Add my commit