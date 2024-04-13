import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
print(sys.getrecursionlimit())


browser = webdriver.Chrome()
browser.get('https://arnypraht.com')
def FindElem(data):
    print(data)
    return browser.find_element(data[0], data[1])

NavData={
    'Сумки': [By.LINK_TEXT, 'Сумки'],
    'Рюкзаки': [By.LINK_TEXT, 'Рюкзаки'],
    'Аксессуары': [By.LINK_TEXT, 'Аксессуары'],
    'Одежда': [By.LINK_TEXT, 'Одежда']
}

def test_Navigation_1():

    click_button = FindElem(NavData['Сумки'])
    print(click_button)
    click_button.click()
    time.sleep(2)

def test_Navigation_2():
    click_button = FindElem(NavData['Рюкзаки'])
    print(click_button)
    click_button.click()
    time.sleep(2)

def test_Navigation_3():
    click_button = FindElem(NavData['Аксессуары'])
    print(click_button)
    click_button.click()
    time.sleep(2)

def test_Navigation_4():
    click_button = FindElem(NavData['Одежда'])
    print(click_button)
    click_button.click()
    time.sleep(2)


