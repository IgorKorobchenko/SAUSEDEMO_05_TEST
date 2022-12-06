#TC001.1-TC001.7 Login with all  possible options for username /pasword
#Expected result User should be directed to the page https://www.saucedemo.com/inventory.html
#or have message about incorrect entered information
import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

Link_mainpage='https://www.saucedemo.com/'
Link_inventory='https://www.saucedemo.com/inventory.html'
Username_valid='standard_user'
Password_valid='secret_sauce'

@pytest.fixture(scope='module')
def browser():
    o = webdriver.FirefoxOptions()
    o.headless = False
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=o)
    yield driver
    driver.quit()

#Check for presence of element on the screen. If element is not in the screen return True
def element_is_not_present(locator):
    try:
        browser.find_element(locator)
        not_found = False
    except:
        not_found = True

    return not_found

def test_login_page_valid(browser):
    """
    TC001.01 Login with valid username and password
    Expected result: User should be directed to the page https://www.saucedemo.com/inventory.html
    """
    browser.get(Link_mainpage)
    browser.find_element(By.ID, 'user-name').send_keys(Username_valid)
    browser.find_element(By.ID, 'password').send_keys(Password_valid)
    browser.find_element(By.ID, 'login-button').click()
    assert browser.current_url == Link_inventory, 'We are on the product page. Test PASSED'

@pytest.mark.parametrize("login, password, rez,exp_message",
  [
      ("","",Link_mainpage,"Epic sadface: Username is required"),
      ("standard_user","",Link_mainpage,"Epic sadface: Password is required"),
      ("","secret_sauce",Link_mainpage,"Epic sadface: Username is required"),
      ("qwerty","asdfgh",Link_mainpage,"Epic sadface: Username and password do not match any user in this service"),
      ("standard_user","zxcvbnm",Link_mainpage,"Epic sadface: Username and password do not match any user in this service"),
      ("qweertyu","secret_sauce",Link_mainpage,"Epic sadface: Username and password do not match any user in this service")
  ]
                         )
def test_login_page_negative(browser,login,password,rez,exp_message):
    """
    TC001.02-TC001.07 Login with some invalid or missed data  for username and/or password
    Expected result: User should stay on the main page https://www.saucedemo.com and error message should be appeared
    """
    browser.get(Link_mainpage)
    browser.find_element(By.ID, 'user-name').send_keys(login)
    browser.find_element(By.ID, 'password').send_keys(password)
    browser.find_element(By.ID, 'login-button').click()

    # identify actual error message
    act_message = browser.find_element(By.XPATH, '//h3[@data-test="error"]').text

    assert browser.current_url == Link_mainpage and act_message==exp_message, "Login rejected"

def test_login_page_close_errormessage(browser):
    """
    TC001.08 Login with some invalid or missed data  for username and/or password so User stays on the main page
    https://www.saucedemo.com and error message appeared
    Expected result: The message should be close after click on X marker
    """
    browser.get(Link_mainpage)
    browser.find_element(By.ID, 'user-name').send_keys("")
    browser.find_element(By.ID, 'password').send_keys("")
    browser.find_element(By.ID, 'login-button').click()
    # click to X mark on button for closing error message
    BTN_error=(By.CSS_SELECTOR,'.error-button>svg')
    browser.find_element(*BTN_error).click()
    #check that message disappered from screen

    assert element_is_not_present(BTN_error)

