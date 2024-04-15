import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



def FindElem(data):
    print(data)
    return browser.find_element(data[0], data[1])

browser = webdriver.Chrome()
browser.get('https://demowebshop.tricentis.com/')

AuthorizationData = {
    'Authorization': [By.CSS_SELECTOR, 'a.ico-login'],
    'Email': [By.CSS_SELECTOR, 'input#Email'],
    'Password': [By.CSS_SELECTOR, 'input#Password'],
    'AuthButton': [By.CSS_SELECTOR, 'div.buttons input[value="Log in"]'],
    'Test': [By.CSS_SELECTOR, 'div.header-links a.account']

}

class TestAuthorization():


    def test_Authorization(self):
        TestEmail = "MeduzaKarapuza@mail.ru"
        TestPassword = "12345678"

        click_button = FindElem(AuthorizationData['Authorization'])
        click_button.click()
        Email = FindElem(AuthorizationData['Email'])
        Email.clear()
        Email.send_keys(TestEmail)
        Password = FindElem(AuthorizationData['Password'])
        Password.clear()
        Password.send_keys(TestPassword)
        time.sleep(2)

        click_button = FindElem(AuthorizationData['AuthButton'])
        click_button.click()
        time.sleep(2)
        Element = FindElem(AuthorizationData['Test'])
        time.sleep(2)
        assert (Element.text == TestEmail)