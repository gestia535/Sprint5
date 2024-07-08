from selenium.webdriver.common.by import By


class TestLocators:
    # Кнопка Войти в аккаунт на Главной
    SEARCH_LOGIN_BUTTON_MAIN_PAGE = By.XPATH, ".//div[@class='BurgerConstructor_basket__container__2fUl3 mt-10']/button[text()='Войти в аккаунт']"

    # Кнопка Зарегистрироваться на странице входа в личный кабинет
    SEARCH_REGISTRATION_BUTTON_LOGIN_ACCOUNT_PAGE = By.XPATH, ".//div[@class='Auth_login__3hAey']//p[1]/a[text()='Зарегистрироваться']"

    # Поле Имя в форме регистрации
    SEARCH_NAME_FIELD_REGISTRATION_FORM = By.XPATH, ".//form/fieldset[1]//input"

    # Поле email в форме регистрации
    SEARCH_EMAIL_FIELD_REGISTRATION_FORM = By.XPATH, ".//form/fieldset[2]//input"

    # Поле пароль в форме регистрации
    SEARCH_PASSWORD_FIELD_REGISTRATION_FORM = By.XPATH, ".//form/fieldset[3]//input"

    # Кнопка Зарегистрироваться в форме регистрации
    SEARCH_REGISTRATION_BUTTON_REGISTRATION_FORM = By.XPATH, ".//form/button[text()='Зарегистрироваться']"

    # Кнопка Личный кабинет на главной
    SEARCH_ACCOUNT_BUTTON_MAIN_PAIGE = By.XPATH, ".//header[@class='AppHeader_header__X9aJA pb-4 pt-4']/nav/a"

    # Кнопка Войти на странице с формой регистрации
    SEARCH_LOGIN_BUTTON_REGISTRATION_FORM = By.XPATH, ".//p/a[text()='Войти']"

    # Поле email в форме входа в ЛК
    SEARCH_EMAIL_FIELD_LOGIN_PAGE = By.XPATH, ".//form/fieldset[1]//input"

    # Поле пароль в форме входа в ЛК
    SEARCH_PASSWORD_FIELD_LOGIN_PAGE = By.XPATH, ".//form/fieldset[2]//input"

    # Кнопка Войти на странице формы входа в ЛК
    SEARCH_LOGIN_BUTTON_LOGIN_PAGE = By.XPATH, ".//div[@class='Auth_login__3hAey']/form/button[text()='Войти']"

    # Кнопка Восстановить пароль на странице с формой входа
    SEARCH_RESTORE_PASSWORD_BUTTON_ACCOUNT_PAGE = By.XPATH, ".//div[@class='Auth_login__3hAey']//p[2]/a[text()='Восстановить пароль']"

    # Кнопка Войти на странице восстановления пароля
    SEARCH_LOGIN_BUTTON_RESTORE_PASSWORD_PAGE = By.XPATH, ".//div[@class='Auth_login__3hAey']//p/a[text()='Войти']"

    # Кнопка Конструктор
    SEARCH_CONSTRUCTOR_BUTTON = By.XPATH, ".//ul[@class='AppHeader_header__list__3oKJj']/li[1]/a"

    # Логотип
    SEARCH_LOGO = By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']/div/a"

    # Кнопка Выход на странице личного кабинета
    SEARCH_EXIT_BUTTON_ACCOUNT_PAGE = By.XPATH, ".//ul/li[3]/button[text()='Выход']"

    # Вкладка Соусы на странице Конструктора
    SEARCH_TAB_SAUCES = By.XPATH, ".//div[@style='display: flex;']/div[2]"

    # Выбранная вкладка Соусы на странице конструктора
    SEARCH_CURRENT_TAB_SAUCES = By.XPATH, ".//main/section[1]/div[1]/div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']"


    # Вкладка Начинки на странице Конструктора
    SEARCH_TAB_FILLINGS = By.XPATH, ".//div[@style='display: flex;']/div[3]"

    # Выбранная вкладка Начинки на странице конструктора
    SEARCH_CURRENT_TAB_FILLINGS = By.XPATH, ".//main/section[1]/div[1]/div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']"

    # Вкладка Булки на странице Конструктора
    SEARCH_TAB_BUNS = By.XPATH, ".//div[@style='display: flex;']/div[1]"

    # Выбранная вкладка Булки на странице конструктора
    SEARCH_CURRENT_TAB_BUNS = By.XPATH, ".//main/section[1]/div[1]/div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']"

    # Некорректный пароль
    SEARCH_ERROR_PASSWORD_MESSAGE_REGISTRATION_PAGE = By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[3]/div/p[@class='input__error text_type_main-default']"

    # Страница с формой входа
    SEARCH_LOGIN_PAGE = By.CLASS_NAME, "Auth_login__3hAey"

    # Кнопка Оформить заказ на главной
    SEARCH_MAKE_ORDER_BUTTON = By.XPATH, ".//main/section[2]/div/button[text()='Оформить заказ']"

    # Заголовок Соберите бургер в разделе Конструктор
    MAKE_BURGER_TITLE = By.XPATH, ".//main/section[1]/h1[text()='Соберите бургер']"


