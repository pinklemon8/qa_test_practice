from tools import *


# Logout
def test_button_logout(login):
    time.sleep(1)
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(1)
    browser.find_element(By.ID, 'logout_sidebar_link').click()
    assert browser.current_url == url, 'Logout is failed'


# About
def test_button_about(login):
    time.sleep(1)
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(1)
    browser.find_element(By.ID, 'about_sidebar_link').click()
    assert browser.current_url == 'https://saucelabs.com/', 'Button "About" does not work'
    browser.quit()


# reset session
@pytest.mark.xfail(reason="fixing this bug right now")
def test_reset_session():
    pass


'''к маркировке xfail можно добавлять параметр reason. Чтобы увидеть это сообщение в консоли, при запуске нужно
добавлять параметр pytest -rx:
pytest lesson1/test_burger_menu.py -rx -s -v --tb=line
'''
