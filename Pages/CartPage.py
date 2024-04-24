from Pages.BasePage import DemoWebShopPage
from conftest import browser
import DataStorage

class CartPages(DemoWebShopPage):

    def clicktoNavBooks(self, browser):
        self.ClickElems(browser, DataStorage.AddCartData['BOOKS'])

    def clicktoProduct(self, browser):
        self.ClickElems(browser, DataStorage.AddCartData['Product'])

    def clicktoCart(self, browser):
        self.ClickElems(browser, DataStorage.AddCartData['Cart'])

    def EnterProduct(self, browser):
        self.EnterData(browser, DataStorage.ChangeCartData['ChangeProduct'], '10')

    def clicktoApply(self, browser):
        self.ClickElems(browser, DataStorage.ChangeCartData['ApplyChange'])

    def checkAddCart(self, browser):
        return self.FindElems(browser, DataStorage.AddCartData['Test'])

    def checkChangeCart(self, browser):
        return self.FindElems(browser, DataStorage.ChangeCartData['Test'])
