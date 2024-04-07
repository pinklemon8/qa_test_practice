from tools import *


# 1. Successfully open url of item card by clicking on item picture
def test_click_pic(login):
    browser.find_element(By.CLASS_NAME, "inventory_item_img").click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', 'Failed opening url'


# 2. Successfully open url of item card by clicking on item name
def test_click_name(login):
    browser.find_element(By.CLASS_NAME, "inventory_item_name").click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', 'Failed opening url'
