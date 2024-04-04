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
    yield
    browser.quit()


# Add_to_cart
def test_add_to_cart(login):
    item_quantity_before = browser.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    item_quantity_after = browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    time.sleep(2)
    assert item_quantity_before != item_quantity_after, 'An item has not been added in the cart.'


# Remove_from_cart
def test_remove_from_cart(login):
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    browser.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
    cart_icon = browser.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert not cart_icon, 'An item has not been removed from the cart.'
