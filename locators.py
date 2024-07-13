from selenium.webdriver.common.by import By


class TestLocators:
    # Кнопка Войти в аккаунт на Главной
    SEARCH_LOGIN_BUTTON_MAIN_PAGE = By.XPATH, "//button[text()='Войти в аккаунт']"

    # Кнопка Зарегистрироваться на странице входа в личный кабинет
    SEARCH_REGISTRATION_BUTTON_LOGIN_ACCOUNT_PAGE = By.XPATH, "//a[text()='Зарегистрироваться']"

    # Поле Имя в форме регистрации
    SEARCH_NAME_FIELD_REGISTRATION_FORM = By.XPATH, "(//input[@name='name' and @type='text'])[1]"

    # Поле email в форме регистрации
    SEARCH_EMAIL_FIELD_REGISTRATION_FORM = By.XPATH, "(//input[@name='name' and @type='text'])[2]"

    # Поле пароль в форме регистрации
    SEARCH_PASSWORD_FIELD_REGISTRATION_FORM = By.XPATH, "//input[@type='password']"

    # Кнопка Зарегистрироваться в форме регистрации
    SEARCH_REGISTRATION_BUTTON_REGISTRATION_FORM = By.XPATH, "//button[text()='Зарегистрироваться']"

    # Кнопка Личный кабинет на главной
    SEARCH_ACCOUNT_BUTTON_MAIN_PAIGE = By.XPATH, "//p[text()='Личный Кабинет']"

    # Кнопка Войти на странице с формой регистрации
    SEARCH_LOGIN_BUTTON_REGISTRATION_FORM = By.XPATH, ".//a[text()='Войти']"

    # Поле email в форме входа в ЛК
    SEARCH_EMAIL_FIELD_LOGIN_PAGE = By.XPATH, "(//input[@name='name' and @type='text'])[1]"

    # Поле пароль в форме входа в ЛК
    SEARCH_PASSWORD_FIELD_LOGIN_PAGE = By.XPATH, "//input[@type='password']"

    # Кнопка Войти на странице формы входа в ЛК
    SEARCH_LOGIN_BUTTON_LOGIN_PAGE = By.XPATH, "//button[text()='Войти']"

    # Кнопка Восстановить пароль на странице с формой входа
    SEARCH_RESTORE_PASSWORD_BUTTON_ACCOUNT_PAGE = By.XPATH, "//a[text()='Восстановить пароль']"

    # Кнопка Войти на странице восстановления пароля
    SEARCH_LOGIN_BUTTON_RESTORE_PASSWORD_PAGE = By.XPATH, "//a[text()='Войти']"

    # Кнопка Конструктор
    SEARCH_CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"

    # Логотип
    SEARCH_LOGO = By.XPATH, "//a[@href='/']"

    # Кнопка Выход на странице личного кабинета
    SEARCH_EXIT_BUTTON_ACCOUNT_PAGE = By.XPATH, "//button[text()='Выход']"

    # Вкладка Соусы на странице Конструктора
    SEARCH_TAB_SAUCES = By.XPATH, ("//div[contains(@class, 'tab_tab__1SPyG') "
                                   "and .//span[@class='text text_type_main-default' and text()='Соусы']]")

    # Выбранная вкладка Соусы на странице конструктора
    SEARCH_CURRENT_TAB_SAUCES = By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Соусы']"

    # Вкладка Начинки на странице Конструктора
    SEARCH_TAB_FILLINGS = By.XPATH, ("//div[contains(@class, 'tab_tab__1SPyG') "
                                     "and .//span[@class='text text_type_main-default' and text()='Начинки']]")

    # Выбранная вкладка Начинки на странице конструктора
    SEARCH_CURRENT_TAB_FILLINGS = By.XPATH, (".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/"
                                             "span[text()='Начинки']")

    # Вкладка Булки на странице Конструктора
    SEARCH_TAB_BUNS = By.XPATH, ("//div[contains(@class, 'tab_tab__1SPyG') "
                                 "and .//span[@class='text text_type_main-default' and text()='Булки']]")

    # Выбранная вкладка Булки на странице конструктора
    SEARCH_CURRENT_TAB_BUNS = By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Булки']"

    # Некорректный пароль
    SEARCH_ERROR_PASSWORD_MESSAGE_REGISTRATION_PAGE = By.CSS_SELECTOR, ".input__error"

    # Страница с формой входа
    SEARCH_LOGIN_PAGE = By.CLASS_NAME, "Auth_login__3hAey"

    # Кнопка Оформить заказ на главной
    SEARCH_MAKE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"

    # Заголовок Соберите бургер в разделе Конструктор
    MAKE_BURGER_TITLE = By.XPATH, "//h1[text()='Соберите бургер']"
