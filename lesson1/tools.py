from selenium import webdriver
import time
import pytest

url = 'https://www.saucedemo.com/'
browser = webdriver.Chrome()


# Фикстура для авторизации
@pytest.fixture()
def login():
    browser.get(url)
    browser.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    browser.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    browser.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(2)
    yield login
