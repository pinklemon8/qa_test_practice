from selenium import webdriver
import pytest

url = 'https://www.saucedemo.com/'
catalog = 'https://www.saucedemo.com/inventory.html'


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()  # Инициализация браузера
    yield driver
    driver.quit()  # Завершение сеанса браузера после выполнения теста
