import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://demowebshop.tricentis.com/')
def FindElem(data):
    print(data)
    return browser.find_element(data[0], data[1])

NavData={
    'BOOKS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/books"]'],
    'COMPUTERS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/computers"]'],
    'ELECTONICS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/electronics'],
    'APPAREL & SHOES': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/apparel-shoes"]'],
    'DIGITAL DOWNLOADS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/digital-downloads"]'],
    'JEWELRY': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/jewelry"]'],
    'GIFT CARDS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/gift-cards"]'],
    'TEST': [By.CSS_SELECTOR, 'div[class="breadcrumb"] strong[class="current-item"]']
}
class TestNav():
    def test_Navigation_1(self):

        click_button = FindElem(NavData['BOOKS'])
        print(click_button)
        click_button.click()
        time.sleep(1)
        current_page = FindElem(NavData['TEST'])
        assert(current_page.text == 'BOOKS')

    def test_Navigation_2(self):

        click_button = FindElem(NavData['COMPUTERS'])
        print(click_button)
        click_button.click()
        time.sleep(1)
        current_page = FindElem(NavData['TEST'])
        assert (current_page.text == 'COMPUTERS')

    def test_Navigation_3(self):

        click_button = FindElem(NavData['ELECTONICS'])
        print(click_button)
        click_button.click()
        time.sleep(1)
        current_page = FindElem(NavData['TEST'])
        assert (current_page.text == 'ELECTRONICS')

    def test_Navigation_4(self):

        click_button = FindElem(NavData['APPAREL & SHOES'])
        print(click_button)
        click_button.click()
        time.sleep(1)
        current_page = FindElem(NavData['TEST'])
        assert (current_page.text == 'APPAREL & SHOES')

    def test_Navigation_5(self):

        click_button = FindElem(NavData['DIGITAL DOWNLOADS'])
        print(click_button)
        click_button.click()
        time.sleep(1)
        current_page = FindElem(NavData['TEST'])
        assert (current_page.text == 'DIGITAL DOWNLOADS')

    def test_Navigation_6(self):

        click_button = FindElem(NavData['JEWELRY'])
        print(click_button)
        click_button.click()
        time.sleep(1)
        current_page = FindElem(NavData['TEST'])
        assert (current_page.text == 'JEWELRY')

    def test_Navigation_7(self):

        click_button = FindElem(NavData['GIFT CARDS'])
        print(click_button)
        click_button.click()
        time.sleep(1)
        current_page = FindElem(NavData['TEST'])
        assert (current_page.text == 'GIFT CARDS')
