import DataStorage
from Pages.BasePage import DemoWebShopPage

from conftest import browser


class SearchPage(DemoWebShopPage):

    def EnterSearch(self, browser):
        self.EnterData(browser, DataStorage.SearchData['Search'], 'science')

    def clicktoButtonSearch(self, browser):
        self.ClickElems(browser, DataStorage.SearchData['Button'])

    def checkSearch(self, browser):
        return self.FindElems(browser, DataStorage.SearchData['Test'])
