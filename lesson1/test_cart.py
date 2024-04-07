from tools import *


# Add_to_cart
def test_add_to_cart(login):
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    cart_badge = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.is_displayed(), 'An item has not been added to cart'


# Remove_from_cart
def test_remove_from_cart(login):
    # browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    # time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    item_in_cart = browser.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]')
    browser.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
    time.sleep(2)
    assert not item_in_cart.is_displayed(), 'An item has not been removed from the cart'


def test_add_from_item(login):
    browser.find_element(By.CLASS_NAME, 'inventory_item_name').click()
    browser.find_element(By.CLASS_NAME, 'btn_inventory').click()
    time.sleep(2)
    shopping_cart_badge = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert shopping_cart_badge.is_displayed(), 'An item has not been added to cart'


def test_remove_from_item(login):
    browser.find_element(By.CLASS_NAME, "inventory_item_name").click()
    browser.find_element(By.XPATH, '//*[@id="remove"]').click()
    time.sleep(2)
    btn_add_to_cart = browser.find_element(By.XPATH, '//*[@id="add-to-cart"]').text
    assert btn_add_to_cart == 'Add to cart', 'Item has not been removed'
    browser.quit()


# pytest lesson1/test_cart.py
