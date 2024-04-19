"""Авто тест с использованием time.sleep()"""
from selenium import webdriver
import time

# Инициализация драйвера
driver = webdriver.Chrome()

# Переход по URL
driver.get("https://victoretc.github.io/selenium_waits/")

# Проверяем заголовок
assert "Практика с ожиданиями в Selenium" in driver.title

# Начинаем тестирование
start_button = driver.find_element_by_id("start_button")
start_button.click()

# Ввод логина и пароля
login_input = driver.find_element_by_id("login_input")
login_input.send_keys("login")
password_input = driver.find_element_by_id("password_input")
password_input.send_keys("password")

# Согласие с правилами
agree_checkbox = driver.find_element_by_id("agree_checkbox")
agree_checkbox.click()

# Нажатие кнопки "Зарегистрироваться"
register_button = driver.find_element_by_id("register_button")
register_button.click()

# Ждем 5 секунд для загрузки и появления сообщения
time.sleep(5)

# Проверяем сообщение
success_message = driver.find_element_by_id("success_message")
assert "Вы успешно зарегистрированы" in success_message.text

# Закрываем браузер
driver.quit()
