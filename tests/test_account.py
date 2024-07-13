from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from test_data import PROFILE_URL


class TestAccount:
    def test_go_to_account_with_account_button_success(self, driver, login):
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_BUTTON_MAIN_PAIGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(PROFILE_URL))

        assert driver.current_url == PROFILE_URL, f'Current url is {driver.current_url}'

    def test_logout_button_success(self, driver, login):
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_BUTTON_MAIN_PAIGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(PROFILE_URL))

        driver.find_element(*TestLocators.SEARCH_EXIT_BUTTON_ACCOUNT_PAGE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_LOGIN_BUTTON_LOGIN_PAGE))

        assert driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_LOGIN_PAGE).is_displayed(), \
            "Entry button is not displayed"
