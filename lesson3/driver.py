import pytest
from selenium import webdriver



@pytest.fixture()
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()

    # Выполняется перед началом тестов
    yield driver

    # Завершение работы драйвера после всех тестов
    driver.quit()
