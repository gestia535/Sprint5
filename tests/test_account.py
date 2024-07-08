from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestAccount:
    def test_go_to_account_with_account_button_success(self, driver, login):
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_BUTTON_MAIN_PAIGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', \
            f'Current url is {driver.current_url}'

    def test_logout_button_success(self, driver, login):
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_BUTTON_MAIN_PAIGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        driver.find_element(*TestLocators.SEARCH_EXIT_BUTTON_ACCOUNT_PAGE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_LOGIN_BUTTON_LOGIN_PAGE))

        assert driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_LOGIN_PAGE).text == 'Войти'
