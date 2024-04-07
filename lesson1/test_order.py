from faker import Faker
from tools import *

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.postcode()


def test_order_finish(login):
    # add item to cart
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    # go to cart
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    # let checkout
    browser.find_element(By.XPATH, '//*[@id="checkout"]').click()
    # enter data: first name, last name, zip/postal code
    browser.find_element(By.ID, 'first-name').send_keys(first_name)
    browser.find_element(By.ID, 'last-name').send_keys(last_name)
    browser.find_element(By.ID, 'postal-code').send_keys(postal_code)
    time.sleep(5)
    # click on the button Continue
    browser.find_element(By.ID, 'continue').click()
    # click on the button Finish
    browser.find_element(By.ID, 'finish').click()
    assert browser.current_url == 'https://www.saucedemo.com/checkout-complete.html'
    time.sleep(2)
    browser.quit()


# pytest lesson1/test_order.py
