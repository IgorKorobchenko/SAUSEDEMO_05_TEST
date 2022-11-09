from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#
# o = webdriver.FirefoxOptions()
# o.headless = True
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=o)
# # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get('https://www.saucedemo.com/')
# usernameId='standard_user'
# passwordId='secret_sauce'
# LOGINNAME='user-name'
# LOGINPASSWORD='password'
# BTN_LOGIN='login-button'
#
#
# def test_login():
#     username_input=driver.find_element(By.ID, LOGINNAME)
#     username_input.send_keys(usernameId)
#     password_input=driver.find_element(By.ID,LOGINPASSWORD)
#     password_input.send_keys(passwordId)
#     driver.find_element(By.ID,BTN_LOGIN).click()
#
#     assert driver.current_url== 'https://www.saucedemo.com/inventory.html'
#
#     driver.quit()



o = webdriver.FirefoxOptions()
o.headless = True
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=o)
driver.get('https://www.saucedemo.com/')
def test_login_page():
    print("Hello")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We are on the product page. Test PASSED'

    driver.quit()
