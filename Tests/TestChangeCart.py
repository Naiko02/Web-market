import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



def FindElem(data):
    print(data)
    return browser.find_element(data[0], data[1])

browser = webdriver.Chrome()
browser.get('https://demowebshop.tricentis.com/')

ChangeCartData = {
    'BOOKS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/books"]'],
    'Product': [By.CSS_SELECTOR, 'input[onclick*="45/1/1"]'],
    'Cart': [By.CSS_SELECTOR, 'a[class="ico-cart"] span[class="cart-label"]'],
    'ChangeProduct': [By.CSS_SELECTOR, 'tbody .qty input'],
    'ApplyChange': [By.NAME, 'updatecart'],
    'Test': [By.CLASS_NAME, 'product-subtotal']

}

class TestChangeCart():
    def test_Change_Cart(self):
        click_button = FindElem(ChangeCartData['BOOKS'])
        click_button.click()
        click_button = FindElem(ChangeCartData['Product'])
        click_button.click()
        click_button = FindElem(ChangeCartData['Cart'])
        click_button.click()
        element=FindElem(ChangeCartData['ChangeProduct'])
        element.clear()
        element.send_keys('10')
        click_button = FindElem(ChangeCartData['ApplyChange'])
        click_button.click()
        Element = FindElem(ChangeCartData['Test'])
        time.sleep(2)
        assert (float(Element.text) == 240.00)