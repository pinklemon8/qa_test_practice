"""Авто тест с использованием Explicit waits и Expected Conditions"""
from driver import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_one(driver):
    # Переход по URL
    driver.get("https://victoretc.github.io/selenium_waits/")

    # Ждем, пока не загрузится страница
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("Практика с ожиданиями в Selenium"))

    # Ждем появления кнопки "Начать тестирование"
    start_button = wait.until(EC.visibility_of_element_located((By.ID, "start_button")))
    start_button.click()

    # Ввод логина и пароля
    login_input = wait.until(EC.visibility_of_element_located((By.ID, "login_input")))
    login_input.send_keys("login")
    password_input = driver.find_element(By.ID, "password_input")
    password_input.send_keys("password")

    # Согласие с правилами
    agree_checkbox = driver.find_element(By.ID, "agree_checkbox")
    agree_checkbox.click()

    # Нажатие кнопки "Зарегистрироваться"
    register_button = driver.find_element(By.ID, "register_button")
    register_button.click()

    # Ждем появления индикатора загрузки и сообщения
    loading_indicator = wait.until(EC.visibility_of_element_located((By.ID, "loading_indicator")))
    success_message = wait.until(EC.visibility_of_element_located((By.ID, "success_message")))

    # Проверяем сообщение
    assert "Вы успешно зарегистрированы" in success_message.text

    # Закрываем браузер
    driver.quit()
