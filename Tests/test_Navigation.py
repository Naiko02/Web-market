import time
import pytest

from conftest import browser
from Pages.NavigationPage import NavigationPage


class TestNavigation:
    def test_books_navigation(self, browser):
        page = NavigationPage(browser)
        page.clicktoNavBooks(browser)
        time.sleep(1)
        assert page.checkNav(browser).text == 'BOOKS'

    def test_computer_navigation(self, browser):
        page = NavigationPage(browser)
        page.clicktoNavComputer(browser)
        time.sleep(1)
        assert page.checkNav(browser).text == 'COMPUTERS'

    def test_electronics_navigation(self, browser):
        page = NavigationPage(browser)
        page.clicktoNavElectronics(browser)
        time.sleep(1)
        assert page.checkNav(browser).text == 'ELECTRONICS'


    def test_apparel_shoes_navigation(self, browser):
        page = NavigationPage(browser)
        page.clicktoNavApparelShoes(browser)
        time.sleep(1)
        assert page.checkNav(browser).text == 'APPAREL & SHOES'

    def test_digital_downloads_navigation(self, browser):
        page = NavigationPage(browser)
        page.clicktoNavDigitalDownloads(browser)
        time.sleep(1)
        assert page.checkNav(browser).text == 'DIGITAL DOWNLOADS'

    def test_jewelry_navigation(self, browser):
        page = NavigationPage(browser)
        page.clicktoNavJewelry(browser)
        time.sleep(1)
        assert page.checkNav(browser).text == 'JEWELRY'

    def test_gift_cards_navigation(self, browser):
        page = NavigationPage(browser)
        page.clicktoNavGiftCards(browser)
        time.sleep(1)
        assert page.checkNav(browser).text == 'GIFT CARDS'




