import pytest
from selenium import webdriver

from helpers import login_generator, password_generator
from locators import TestLocators
from test_data import BASE_URL, TEST_EMAIL, TEST_PASSWORD


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(BASE_URL)
    driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
    driver.find_element(*TestLocators.SEARCH_EMAIL_FIELD_LOGIN_PAGE).send_keys(TEST_EMAIL)
    driver.find_element(*TestLocators.SEARCH_PASSWORD_FIELD_LOGIN_PAGE).send_keys(TEST_PASSWORD)
    driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_LOGIN_PAGE).click()
    driver.find_element(*TestLocators.SEARCH_ACCOUNT_BUTTON_MAIN_PAIGE).click()
    yield driver


@pytest.fixture()
def data_generator():
    domain = 'gmail.com'
    email, first_name = login_generator(domain)
    password = password_generator()
    return email, first_name, password
