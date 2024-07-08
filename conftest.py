import pytest
from selenium import webdriver

from locators import TestLocators


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
    driver.find_element(*TestLocators.SEARCH_EMAIL_FIELD_LOGIN_PAGE).send_keys('pavliukova_11@gmail.com')
    driver.find_element(*TestLocators.SEARCH_PASSWORD_FIELD_LOGIN_PAGE).send_keys('1111111')
    driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_LOGIN_PAGE).click()
    driver.find_element(*TestLocators.SEARCH_ACCOUNT_BUTTON_MAIN_PAIGE).click()
    yield driver
