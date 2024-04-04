import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.saucedemo.com/'
catalog = 'https://www.saucedemo.com/inventory.html'
browser = webdriver.Chrome()


# Фикстура для авторизации
@pytest.fixture()
def login():
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys('standard_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").click()
    yield login
    browser.quit()


# Add_to_cart
def test_add_to_cart(login):
    add_to_cart_buttons = browser.find_elements(By.CLASS_NAME, 'add-to-cart-button')
    add_to_cart_buttons[1].click()
    assert browser.find_element(By.CLASS_NAME, 'remove-from-cart-button').text == 'Remove', ('An item has not been '
                                                                                             'added to cart')


# Remove_from_cart
def test_remove_from_cart(login):
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    browser.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
    cart_icon = browser.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert not cart_icon, 'An item has not been removed from the cart.'
