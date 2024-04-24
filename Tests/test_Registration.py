import time
import pytest
from conftest import browser
from Pages.RegistrationPage import RegPage

class TestRegistration:
    def test_Reg(self, browser):
        page = RegPage(browser)
        page.clicktoReg(browser)
        time.sleep(1)
        page.clicktoGender(browser)
        page.EnterFirstName(browser)
        page.EnterLastName(browser)
        page.EnterEmail(browser)
        page.EnterPassword(browser)
        page.EnterConfirm(browser)
        time.sleep(1)
        page.clicktoButtonReg(browser)

        assert page.checkReg(browser).text == DataSt.TestData['TestEmail']
