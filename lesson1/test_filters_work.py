from tools import *


def test_filter_A_to_Z(login):
    browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]').click()
    time.sleep(2)
    # Check sorting
    items_names = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert sorted([name.text for name in items_names]) == [name.text for name in items_names], ('Filter Name (A to Z) '
                                                                                                'does not work')


def test_filter_Z_to_A(login):
    browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]').click()
    time.sleep(2)
    # Check sorting
    items_names = browser.find_elements(By.XPATH, '//*[@id="inventory_container"]')
    assert sorted([name.text for name in items_names]) == [name.text for name in items_names], ('Filter Name (Z to A) '
                                                                                                'does not work')


def test_price_low_to_high(login):
    browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]').click()
    time.sleep(2)
    # Find all elements include the prices of items
    items_prices = browser.find_elements(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    # Remove $ from the prices
    prices = [float(item_price.text.replace('$', '')) for item_price in items_prices]
    # Check sorting
    assert prices == sorted(prices), 'Filter price(low to high) does not work'


def test_price_high_to_low(login):
    browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]').click()
    time.sleep(2)
    # Find all elements include the prices of items
    items_prices = browser.find_elements(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    # Remove $ from the prices
    prices = [float(item_price.text.replace('$', '')) for item_price in items_prices]
    # Check sorting
    assert prices == sorted(prices), 'Filter price(high to low) does not work'
    browser.quit()
