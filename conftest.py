import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.quit()
