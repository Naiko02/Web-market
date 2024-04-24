import time
from conftest import browser
from Pages.FilterPage import FilterPage
import pytest

class TestFilter:
    def test_search(self, browser):
        page = FilterPage(browser)
        page.clicktoNavBooks(browser)
        time.sleep(1)
        page.clicktoFilter(browser)
        time.sleep(2)

        assert page.checkFilter(browser).text == 'Science'
