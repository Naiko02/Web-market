from Pages.BasePage import DemoWebShopPage
import DataStorage
from conftest import browser

class NavigationPage(DemoWebShopPage):

    def clicktoNavBooks(self, browser):
        self.ClickElems(browser, DataStorage.nav_data['BOOKS'])

    def clicktoNavComputer(self, browser):
        self.ClickElems(browser, DataStorage.nav_data['COMPUTERS'])

    def clicktoNavElectronics(self, browser):
        self.ClickElems(browser, DataStorage.nav_data['ELECTRONICS'])

    def clicktoNavApparelShoes(self, browser):
        self.ClickElems(browser, DataStorage.nav_data['APPAREL & SHOES'])

    def clicktoNavDigitalDownloads(self, browser):
        self.ClickElems(browser, DataStorage.nav_data['DIGITAL DOWNLOADS'])

    def clicktoNavJewelry(self, browser):
        self.ClickElems(browser, DataStorage.nav_data['JEWELRY'])

    def clicktoNavGiftCards(self, browser):
        self.ClickElems(browser, DataStorage.nav_data['GIFT CARDS'])

    def checkNav(self, browser):
        return self.FindElems(browser, DataStorage.nav_data['TEST'])