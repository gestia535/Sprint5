from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from test_data import BASE_URL, TEST_EMAIL, TEST_PASSWORD


class TestLogin:
    def test_login_with_login_button_main_page_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_EMAIL_FIELD_LOGIN_PAGE).send_keys(TEST_EMAIL)
        driver.find_element(*TestLocators.SEARCH_PASSWORD_FIELD_LOGIN_PAGE).send_keys(TEST_PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_MAKE_ORDER_BUTTON))

        assert driver.find_element(*TestLocators.SEARCH_MAKE_ORDER_BUTTON).is_displayed(), \
            "Order button is not displayed"

    def test_login_with_account_button_main_page_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_BUTTON_MAIN_PAIGE).click()
        driver.find_element(*TestLocators.SEARCH_EMAIL_FIELD_LOGIN_PAGE).send_keys(TEST_EMAIL)
        driver.find_element(*TestLocators.SEARCH_PASSWORD_FIELD_LOGIN_PAGE).send_keys(TEST_PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_LOGIN_PAGE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_MAKE_ORDER_BUTTON))

        assert driver.find_element(*TestLocators.SEARCH_MAKE_ORDER_BUTTON).is_displayed(), \
            "Order button is not displayed"

    def test_login_from_registration_page_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_BUTTON_LOGIN_ACCOUNT_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_REGISTRATION_FORM).click()

        driver.find_element(*TestLocators.SEARCH_EMAIL_FIELD_LOGIN_PAGE).send_keys(TEST_EMAIL)
        driver.find_element(*TestLocators.SEARCH_PASSWORD_FIELD_LOGIN_PAGE).send_keys(TEST_PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_LOGIN_PAGE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_MAKE_ORDER_BUTTON))

        assert driver.find_element(*TestLocators.SEARCH_MAKE_ORDER_BUTTON).is_displayed(), \
            "Order button is not displayed"

    def test_login_from_restore_password_page_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_BUTTON_MAIN_PAIGE).click()
        driver.find_element(*TestLocators.SEARCH_RESTORE_PASSWORD_BUTTON_ACCOUNT_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_RESTORE_PASSWORD_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_EMAIL_FIELD_LOGIN_PAGE).send_keys(TEST_EMAIL)
        driver.find_element(*TestLocators.SEARCH_PASSWORD_FIELD_LOGIN_PAGE).send_keys(TEST_PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_LOGIN_PAGE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_MAKE_ORDER_BUTTON))

        assert driver.find_element(*TestLocators.SEARCH_MAKE_ORDER_BUTTON).is_displayed(), \
            "Order button is not displayed"
