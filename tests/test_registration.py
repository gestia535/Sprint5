from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from test_data import BASE_URL, LOGIN_URL


class TestRegistration:
    def test_registration_success(self, driver, data_generator):
        email, first_name, password = data_generator
        driver.get(BASE_URL)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_BUTTON_LOGIN_ACCOUNT_PAGE).click()

        elm_name = driver.find_element(*TestLocators.SEARCH_NAME_FIELD_REGISTRATION_FORM)
        elm_email = driver.find_element(*TestLocators.SEARCH_EMAIL_FIELD_REGISTRATION_FORM)
        elm_password = driver.find_element(*TestLocators.SEARCH_PASSWORD_FIELD_REGISTRATION_FORM)

        elm_name.send_keys(first_name)
        elm_email.send_keys(email)
        elm_password.send_keys(password)
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_BUTTON_REGISTRATION_FORM).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(LOGIN_URL))

        assert driver.current_url == LOGIN_URL, f'Current url is {driver.current_url}'

    def test_registration_short_password_failed(self, driver, data_generator):
        email, first_name, password = data_generator
        driver.get(BASE_URL)
        driver.find_element(*TestLocators.SEARCH_LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_BUTTON_LOGIN_ACCOUNT_PAGE).click()

        elm_name = driver.find_element(*TestLocators.SEARCH_NAME_FIELD_REGISTRATION_FORM)
        elm_email = driver.find_element(*TestLocators.SEARCH_EMAIL_FIELD_REGISTRATION_FORM)
        elm_password = driver.find_element(*TestLocators.SEARCH_PASSWORD_FIELD_REGISTRATION_FORM)

        elm_name.send_keys(first_name)
        elm_email.send_keys(email)
        elm_password.send_keys('11')
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_BUTTON_REGISTRATION_FORM).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                TestLocators.SEARCH_ERROR_PASSWORD_MESSAGE_REGISTRATION_PAGE))

        elm_wrong_pass = driver.find_element(*TestLocators.SEARCH_ERROR_PASSWORD_MESSAGE_REGISTRATION_PAGE)
        assert elm_wrong_pass.text == 'Некорректный пароль'
