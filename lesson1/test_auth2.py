from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

url = 'https://www.saucedemo.com/'
catalog = 'https://www.saucedemo.com/inventory.html'


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def login(browser, username, password):
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()


@pytest.mark.parametrize("username, password", [
    ('standard_user', 'secret_sauce'),
    ('locked_out_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('error_user', 'secret_sauce'),
    ('visual_user', 'secret_sauce'),
])
def test_login(browser, username, password):
    login(browser, username, password)
    if username == 'locked_out_user':
        error_message_text = 'Epic sadface: Sorry, this user has been locked out.'
        assert error_message_text in browser.page_source, 'Expected error message not found'
        assert browser.current_url == url, 'Expected to stay on login page'
    else:
        assert browser.current_url == catalog, f'Authorisation unsuccessful'


def test_negative(browser):
    login(browser, 'user', 'user')
    assert browser.current_url != catalog, 'Expected authorisation to be failed'
    print('Epic sadface: Username and password do not match any user in this service')
    time.sleep(2)
