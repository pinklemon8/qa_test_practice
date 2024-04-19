"""Авто тест с использованием Implicit waits"""
from selenium import webdriver

# Устанавливаем неявное ожидание
driver = webdriver.Chrome()
driver.implicitly_wait(10)

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

# Проверка индикатора загрузки и сообщения
loading_indicator = driver.find_element_by_id("loading_indicator")
success_message = driver.find_element_by_id("success_message")

# Проверяем сообщение
assert "Вы успешно зарегистрированы" in success_message.text

# Закрываем браузер
driver.quit()
