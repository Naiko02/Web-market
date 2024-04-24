from Pages.BasePage import DemoWebShopPage
import DataStorage
from conftest import browser

class RegPage(DemoWebShopPage):

    def clicktoReg(self, browser):

        self.ClickElems(browser, DataStorage.RegistrationData['Registration'])

    def clicktoGender(self, browser):

        self.ClickElems(browser, DataStorage.RegistrationData['Gender'])

    def EnterFirstName(self, browser):
        self.EnterData(browser, DataStorage.RegistrationData['FirstName'], 'Викторус')

    def EnterLastName(self, browser):
        self.EnterData(browser, DataStorage.RegistrationData['LastName'], 'Володин')

    def EnterEmail(self, browser):
        self.EnterData(browser, DataStorage.RegistrationData['Email'], DataStorage.TestData['TestEmail'])

    def EnterPassword(self, browser):
        self.EnterData(browser, DataStorage.RegistrationData['Password'], DataStorage.TestData['TestPassword'])

    def EnterConfirm(self, browser):
        self.EnterData(browser, DataStorage.RegistrationData['Confirm'], DataStorage.TestData['TestPassword'])


    def clicktoButtonReg(self, browser):
        self.ClickElems(browser, DataStorage.RegistrationData['RegButton'])

    def checkReg(self, browser):
        return self.FindElems(browser, DataStorage.RegistrationData['Test'])
