import pytest
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.saucedemo.com/'
catalog = 'https://www.saucedemo.com/inventory.html'


@pytest.fixture()
def auth():
    print("\nstart browser for test..")
    browser.get(url)
    yield browser
    print("\nquit browser..")
    browser.quit()
