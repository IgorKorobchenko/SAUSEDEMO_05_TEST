import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

o = webdriver.FirefoxOptions()
o.headless = True
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=o)
driver.get('https://www.saucedemo.com/')

#TC003.1
def test_filter_button_open_options():
    user_login()
    FilterSelector=driver.find_element(By.CLASS_NAME,'product_sort_container')
    FilterSelector.click()
    # verify the dropdown is enabled & visible
    assert (FilterSelector.is_enabled()&FilterSelector.is_displayed()) , "User can open dropdown filter options"
    driver.quit()

    # driver.quit()
#TC003.3
# def test_filter_button_choose_options():
#     user_login()
#     FilterSelector = driver.find_element(By.CLASS_NAME, 'product_sort_container')
#     FilterSelector.click()
#     FilterAZ = driver.find_element(By.XPATH, '//option[@value="az"]')
#     FilterAZ.click()
#     # verify the dropdown is enabled & visible
#     assert (DropdownElement.is_enabled()&DropdownElement.is_displayed()) , "User can open dropdodown filter options"
#
#     driver.quit()

