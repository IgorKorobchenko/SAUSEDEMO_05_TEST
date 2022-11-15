import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

import conf


@pytest.fixture()
def b(browser):
    driver = None
    if browser == 'chrome':
        o = webdriver.ChromeOptions()
        o.headless = True  #conf.BROWSER_HEADLESS
        driver = webdriver.Chrome(
            service=ChromiumService(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=o,
        )
    else:
        o = webdriver.FirefoxOptions()
        o.headless = True  #conf.BROWSER_HEADLESS
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=o
        )
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="firefox",
        help="define browser: chrome or firefox, --browser=chrome",
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(autouse=True)
def g(b):
    print('\n*** start fixture = setup ***\n')
    b.get('https://www.saucedemo.com/')                                   #conf.URL)
    b.find_element(By.ID, "user-name").send_keys("standard_user")
    b.find_element(By.ID, "password").send_keys("secret_sauce")
    b.find_element(By.ID, "login-button").click()
    time.sleep(2)
    b.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    b.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    b.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    time.sleep(2)

    yield b
    b.quit()
    print('\n*** end fixture = teardown ***\n')


def pytest_html_report_title(report):
    report.title = "Kate Fox"