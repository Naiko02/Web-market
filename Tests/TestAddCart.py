import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By



def FindElem(data):
    print(data)
    return browser.find_element(data[0], data[1])

browser = webdriver.Chrome()
browser.get('https://demowebshop.tricentis.com/')

AddCartData = {
    'BOOKS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/books"]'],
    'Product': [By.CSS_SELECTOR, 'input[onclick*="45/1/1"]'],
    'Cart': [By.CSS_SELECTOR, 'a[class="ico-cart"] span[class="cart-label"]'],
    'Test': [By.CSS_SELECTOR, 'a[class="product-name"][href*=fiction]']

}

class TestAddCart():
    def test_Add_Cart(self):
        click_button = FindElem(AddCartData['BOOKS'])
        click_button.click()
        click_button=FindElem(AddCartData['Product'])
        click_button.click()
        click_button = FindElem(AddCartData['Cart'])
        click_button.click()
        Element = FindElem(AddCartData['Test'])
        time.sleep(2)
        assert (Element.text == 'Fiction')