import time
import DataStorage
from conftest import browser
from Pages.AuthorizationPage import AuthPage
import pytest


class TestAuthorization:
    def test_Auth(self, browser):
        page = AuthPage(browser)
        page.clicktoAuth(browser)
        time.sleep(1)
        page.EnterEmail(browser)
        page.EnterPassword(browser)
        time.sleep(1)
        page.clicktoButtonAuth(browser)

        assert page.checkAuth(browser).text == DataStorage.TestData['TestEmail']
