from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

browser = webdriver.Chrome()
url = 'https://www.saucedemo.com/'
catalog = 'https://www.saucedemo.com/inventory.html'


@pytest.fixture  # Authorization fixture
def login():
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('standard_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)
    yield login
    browser.quit()
