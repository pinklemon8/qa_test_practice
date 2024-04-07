from tools import *


# 1. Successful navigation to the item card after clicking on the item image
def test_click_pic(login):
    browser.find_element(By.CLASS_NAME, "inventory_item_img").click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', 'Navigation failed'


# 2. Successful navigation to the item card after clicking on the item name
def test_click_name(login):
    browser.find_element(By.CLASS_NAME, "inventory_item_name").click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', 'Navigation failed'
    browser.quit()

# pytest lesson1/test_item_card.py
