import time
import pytest
from conftest import browser
from Pages.SearchPage import SearchPage

class TestSearch:
    def test_search(self, browser):
        page = SearchPage(browser)
        page.EnterSearch(browser)
        time.sleep(1)
        page.clicktoButtonSearch(browser)
        time.sleep(2)

        assert page.checkSearch(browser).text == 'Science'
