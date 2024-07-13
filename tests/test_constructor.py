from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from test_data import BASE_URL, PROFILE_URL


class TestConstructor:
    def test_go_to_constructor_with_constructor_button_success(self, driver, login):
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(PROFILE_URL))

        driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR_BUTTON).click()

        assert driver.find_element(*TestLocators.MAKE_BURGER_TITLE).is_displayed(), \
            'Make burger button is not displayed'

    def test_go_to_constructor_with_logo_button_success(self, driver, login):
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(PROFILE_URL))

        driver.find_element(*TestLocators.SEARCH_LOGO).click()

        assert driver.find_element(*TestLocators.MAKE_BURGER_TITLE).is_displayed(), \
            'Make burger button is not displayed'

    def test_go_to_sauces_tab_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*TestLocators.SEARCH_TAB_SAUCES).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.SEARCH_CURRENT_TAB_SAUCES))

        assert driver.find_element(*TestLocators.SEARCH_CURRENT_TAB_SAUCES).is_displayed(), f'Tab is not displayed'

    def test_go_to_fillings_tab_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*TestLocators.SEARCH_TAB_FILLINGS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.SEARCH_CURRENT_TAB_FILLINGS))

        assert driver.find_element(*TestLocators.SEARCH_CURRENT_TAB_FILLINGS).is_displayed(), f'Tab is not displayed'

    def test_go_to_buns_tab_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*TestLocators.SEARCH_TAB_FILLINGS).click()
        driver.find_element(*TestLocators.SEARCH_TAB_BUNS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                       (TestLocators.SEARCH_CURRENT_TAB_BUNS))

        assert driver.find_element(*TestLocators.SEARCH_CURRENT_TAB_BUNS).is_displayed(), f'Tab is not displayed'
