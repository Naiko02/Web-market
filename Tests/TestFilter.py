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

FilterData = {
    'BOOKS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/books"]'],
    'Filter': [By.CSS_SELECTOR, 'a[href*="=50"]'],
    'Test': [By.CSS_SELECTOR, 'h2[class="product-title"] a[href$="science"]']

}

class TestFilter():
    def test_Filter(self):
        click_button = FindElem(FilterData['BOOKS'])
        click_button.click()
        click_button=FindElem(FilterData['Filter'])
        click_button.click()
        Element = FindElem(FilterData['Test'])
        time.sleep(2)
        assert (Element.text == 'Science')