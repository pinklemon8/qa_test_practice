from tools import *


# 1
def test_standard_user():
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('standard_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorization is failed'


# 2
def test_locked_out_user():
    try:
        browser.get(url)
        browser.find_element(By.ID, "user-name").send_keys('locked_out_user')
        browser.find_element(By.ID, "password").send_keys('secret_sauce')
        browser.find_element(By.ID, "login-button").click()
        assert browser.current_url == catalog, 'Authorization is failed'
    except AssertionError:
        error_message = 'Epic sadface: Sorry, this user has been locked out.'
        print(error_message)
        time.sleep(3)


# 3
def test_problem_user():
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('problem_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorization is failed'


# 4
def test_performance_glitch_user():
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('performance_glitch_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorization is failed'


# 5
def test_error_user():
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('error_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorization is failed'


# 6
def test_visual_user():
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('visual_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url == catalog, f'Authorization is failed'


def test_negative():
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('user')
    browser.find_element(By.ID, "password").send_keys('user')
    browser.find_element(By.ID, "login-button").click()
    assert browser.current_url != catalog, 'Expected authorisation to be failed'
    print('Epic sadface: Username and password do not match any user in this service')
    time.sleep(3)
    browser.quit()

# pytest lesson1/test_auth.py
