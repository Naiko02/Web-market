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

RegistrationData = {
    'Registration': [By.CSS_SELECTOR, 'a.ico-register'],
    'Gender': [By.CSS_SELECTOR, 'input#gender-male'],
    'FirstName': [By.CSS_SELECTOR, 'input#FirstName'],
    'LastName': [By.CSS_SELECTOR, 'input#LastName'],
    'Email': [By.CSS_SELECTOR, 'input#Email'],
    'Password': [By.CSS_SELECTOR, 'input#Password'],
    'Confirm': [By.CSS_SELECTOR, 'input#ConfirmPassword'],
    'RegButton': [By.ID, 'register-button'],
    'Test': [By.CSS_SELECTOR, 'div.header-links a.account']

}

class TestRegistration():


    def test_Registration(self):
        TestEmail = "MeduzaKarapuzas@mail.ru"
        TestPassword = "12345678"

        click_button = FindElem(RegistrationData['Registration'])
        click_button.click()
        click_button = FindElem(RegistrationData['Gender'])
        click_button.click()
        FirstName = FindElem(RegistrationData['FirstName'])
        FirstName.clear()
        FirstName.send_keys('Викторус')
        LastName = FindElem(RegistrationData['LastName'])
        LastName.clear()
        LastName.send_keys('Володин')
        Email = FindElem(RegistrationData['Email'])
        Email.clear()
        Email.send_keys(TestEmail)
        Password = FindElem(RegistrationData['Password'])
        Password.clear()
        Password.send_keys(TestPassword)
        ConfirmPassword = FindElem(RegistrationData['Confirm'])
        ConfirmPassword.clear()
        ConfirmPassword.send_keys(TestPassword)
        time.sleep(2)

        click_button = FindElem(RegistrationData['RegButton'])
        click_button.click()
        time.sleep(2)
        Element = FindElem(RegistrationData['Test'])
        time.sleep(2)
        assert (Element.text == TestEmail)