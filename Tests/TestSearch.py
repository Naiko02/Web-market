import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By



def FindElem(data):
    print(data)
    return browser.find_element(data[0], data[1])


SearchData={
    'Search': [By.ID, 'small-searchterms'],
    'Button': [By.CSS_SELECTOR, 'input[value="Search"]'],
    'Test': [By.CSS_SELECTOR, 'h2[class="product-title"] a[href$="science"]']
}

browser = webdriver.Chrome()
browser.get('https://demowebshop.tricentis.com/')

class TestFind():
    def test_Find(self):
        FindElem(SearchData['Search']).send_keys('science')
        click_button = FindElem(SearchData['Button'])
        click_button.click()
        Element=FindElem(SearchData['Test'])
        time.sleep(2)
        assert (Element.text == 'Science')
