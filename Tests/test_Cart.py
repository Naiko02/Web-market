import time
from conftest import browser
from Pages.CartPage import CartPages
import pytest

class TestCart:
    def test_add_cart(self, browser):
        page = CartPages(browser)
        page.clicktoNavBooks(browser)
        time.sleep(1)
        page.clicktoProduct(browser)
        page.clicktoCart(browser)
        time.sleep(2)

        assert page.checkAddCart(browser).text == 'Fiction'

    def test_change_cart(self, browser):
        page = CartPages(browser)
        page.EnterProduct(browser)
        time.sleep(1)
        page.clicktoApply(browser)
        time.sleep(2)

        assert float(page.checkChangeCart(browser).text) == 240.00

