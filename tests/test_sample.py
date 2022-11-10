# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager




def test_sample():
    # o = webdriver.FirefoxOptions()
    # o.headless = True
    # driver = webdriver.Chrome(
    #     service=ChromeService(ChromeDriverManager().install())), options=o
    # )

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    assert driver.title == "Swag Labs"

    driver.quit()
