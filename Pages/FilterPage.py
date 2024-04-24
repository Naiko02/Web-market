from Pages.BasePage import DemoWebShopPage
import DataStorage
from conftest import browser




class FilterPage(DemoWebShopPage):

    def clicktoNavBooks(self, browser):
        self.ClickElems(browser, DataStorage.FilterData['BOOKS'])

    def clicktoFilter(self, browser):
        self.ClickElems(browser, DataStorage.FilterData['Filter'])

    def checkFilter(self, browser):
        return self.FindElems(browser, DataStorage.FilterData['Test'])
