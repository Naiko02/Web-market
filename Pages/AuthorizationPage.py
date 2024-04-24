from Pages.BasePage import DemoWebShopPage
import DataStorage
from conftest import browser




class AuthPage(DemoWebShopPage):

    def clicktoAuth(self, browser):

        self.ClickElems(browser, DataStorage.AuthorizationData['Authorization'])

    def EnterEmail(self, browser):
        self.EnterData(browser, DataStorage.AuthorizationData['Email'], DataStorage.TestData['TestEmail'])

    def EnterPassword(self, browser):
        self.EnterData(browser, DataStorage.AuthorizationData['Password'], DataStorage.TestData['TestPassword'])


    def clicktoButtonAuth(self, browser):
        self.ClickElems(browser, DataStorage.AuthorizationData['AuthButton'])

    def checkAuth(self, browser):
        return self.FindElems(browser, DataStorage.AuthorizationData['Test'])
