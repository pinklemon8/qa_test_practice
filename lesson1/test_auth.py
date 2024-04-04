from tools import *
from selenium.webdriver.common.by import By


# 1
def test_standard_user(browser):
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('standard_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorisation unsuccessful'


# 2
def test_locked_out_user(browser):
    try:
        browser.get(url)
        browser.find_element(By.ID, "user-name").send_keys('locked_out_user')
        browser.find_element(By.ID, "password").send_keys('secret_sauce')
        browser.find_element(By.ID, "login-button").click()
        assert browser.current_url == catalog, 'Authorisation unsuccessful'
    except AssertionError:
        print(f'Epic sadface: Sorry, this user has been locked out.')

    # 3


def test_problem_user(browser):
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('problem_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorisation unsuccessful'


# 4
def test_performance_glitch_user(browser):
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('performance_glitch_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorisation unsuccessful'


# 5
def test_error_user(browser):
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('error_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorisation unsuccessful'


# 6
def test_visual_user(browser):
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('visual_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorisation unsuccessful'
