from selenium.webdriver.remote.webdriver import WebDriver


class DemoWebShopPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def ClickElems(self, browser, category):

         self.driver.find_element(category[0], category[1]).click()
    def FindElems(self, browser, category):

         return self.driver.find_element(category[0], category[1])

    def EnterData(self, browser, FindData, data):
        self.FindElems(browser, FindData).clear()
        self.FindElems(browser, FindData).send_keys(data)
