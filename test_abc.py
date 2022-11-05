import time
from webbrowser import BaseBrowser
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

driver.get('https://abcmouse.com.vn/')

MainPage = driver.find_element(By.XPATH, '//*[@id="basic-navbar-nav"]/div/a[4]').click()

LoginPage = driver.find_element(By.XPATH, '//*[@id="phone-number-login"]')
LoginPage.send_keys('0301291111')

loginButton = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div/div/div[2]/div[3]/div')

time.sleep(2.0)

loginButton.click()

time.sleep(2.0)

otpBox1 =driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/input')
otpBox1.send_keys('0')
time.sleep(2.0)

otpBox2 =driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/input')
otpBox2.send_keys('1')
time.sleep(2.0)

otpBox3 =driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div/div[2]/div[3]/div[2]/div[1]/div[3]/input')
otpBox3.send_keys('2')
time.sleep(2.0)

otpBox4 =driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div/div[2]/div[3]/div[2]/div[1]/div[4]/input')
otpBox4.send_keys('9')
time.sleep(2.0)

submitButton = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div/div[2]/div[4]')
time.sleep(2.0)

submitButton.click ()
time.sleep(2.0)

dropdown= driver.find_element(By.XPATH,'//*[@id="__next"]/main/header/div/div/div/span')

dropdown.click()

logout = driver.find_element(By.XPATH, '//*[@id="__next"]/main/header/div/div/div/div/span[2]')
logout.click()

finalbutton = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[3]/button[2]')

finalbutton.click()

driver.quit()







#loginBox = driver.find_element(By.XPATH, '//*[@id="phone-number-login"]')

#loginBox = driver.send_keys('vn@vn.vn')

#loginButton = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div/div/div[2]/div[3]/div').click



