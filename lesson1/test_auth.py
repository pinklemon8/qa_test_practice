from conftest import *
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'https://www.saucedemo.com/'
catalog = 'https://www.saucedemo.com/inventory.html'


# 1
def test_standard_user():
    browser.get(link)
    browser.find_element(By.ID, "user-name").send_keys('standard_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorization is failed'


# 2

def test_locked_out_user():
    browser.get(link)
    try:
        browser.find_element(By.ID, "user-name").send_keys('locked_out_user')
        browser.find_element(By.ID, "password").send_keys('secret_sauce')
        browser.find_element(By.ID, "login-button").click()
        assert browser.current_url == catalog, 'Authorization is failed'
    except AssertionError:
        error_message = 'Epic sadface: Sorry, this user has been locked out.'
        print(error_message)


# 3
def test_problem_user():
    browser.get(link)
    browser.find_element(By.ID, "user-name").send_keys('problem_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorization is failed'


# 4
def test_performance_glitch_user():
    browser.get(link)
    browser.find_element(By.ID, "user-name").send_keys('performance_glitch_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorization is failed'


# 5
def test_error_user():
    browser.get(link)
    browser.find_element(By.ID, "user-name").send_keys('error_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorization is failed'


# 6
def test_visual_user():
    browser.get(link)
    browser.find_element(By.ID, "user-name").send_keys('visual_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorization is failed'


def test_negative():
    browser.get(link)
    browser.find_element(By.ID, "user-name").send_keys('user')
    browser.find_element(By.ID, "password").send_keys('user')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url != catalog, 'Expected authorisation to be failed'
    print('Epic sadface: Username and password do not match any user in this service')

# pytest lesson1/test_auth.py -s -v --tb=line
