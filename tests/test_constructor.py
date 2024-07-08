from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestConstructor:
    def test_go_to_constructor_with_constructor_button_success(self, driver, login):
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR_BUTTON).click()

        assert driver.find_element(*TestLocators.MAKE_BURGER_TITLE).text == 'Соберите бургер'

    def test_go_to_constructor_with_logo_button_success(self, driver, login):
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        driver.find_element(*TestLocators.SEARCH_LOGO).click()

        assert driver.find_element(*TestLocators.MAKE_BURGER_TITLE).text == 'Соберите бургер'

    def test_go_to_sauces_tab_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_TAB_SAUCES).click()

        assert driver.find_element(*TestLocators.SEARCH_CURRENT_TAB_SAUCES).text == 'Соусы'

    def test_go_to_fillings_tab_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_TAB_FILLINGS).click()

        assert driver.find_element(*TestLocators.SEARCH_CURRENT_TAB_FILLINGS).text == 'Начинки'

    def test_go_to_buns_tab_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_TAB_FILLINGS).click()
        driver.find_element(*TestLocators.SEARCH_TAB_BUNS).click()

        assert driver.find_element(*TestLocators.SEARCH_CURRENT_TAB_BUNS).text == 'Булки'
