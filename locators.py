from selenium.webdriver.common.by import By


class Locators:
    # --- Кнопка "Вход и регистрация" в шапке ---
    ENTER_AND_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button.buttonSecondary")

    # --- Общая форма модалки логина/регистрации ---
    # Это <form> внутри модального окна
    REGISTRATION_FORM = (By.CSS_SELECTOR, ".popUp_shell__LuyqR")

    # Оверлей/контейнер модалки (если где-то нужен)
    HOME_PAGE_MODAL = (By.CSS_SELECTOR, ".homePage_modal__zSdUB")

    # Синоним, если старый код использует LOGIN_FORM
    LOGIN_FORM = REGISTRATION_FORM

    # --- Поле Email в модалках логина/регистрации ---
    EMAIL_INPUT = (
        By.XPATH,
        "//div[contains(@class,'homePage_modal__zSdUB')]"
        "//input[@name='email' or @type='email' or @placeholder='Введите Email']"
    )

    # --- 1-е поле пароля (основной пароль) ---
    PASSWORD_INPUT = (
        By.XPATH,
        "//div[contains(@class,'homePage_modal__zSdUB')]//input[@type='password'][1]"
    )

    # --- 2-е поле пароля (повтор пароля) ---
    PASSWORD_CONFIRM_INPUT = (
        By.CSS_SELECTOR,
        "input[name='submitPassword']"
    )

    # --- Кнопка "Нет аккаунта" ---
    HAVE_NOT_ACCOUNT = (
        By.XPATH,
        "//div[contains(@class,'homePage_modal__zSdUB')]"
        "//button[normalize-space()='Нет аккаунта']"
    )

    # --- Кнопка "Создать аккаунт" (регистрация) ---
    REGISTRATION_SUBMIT_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'homePage_modal__zSdUB')]"
        "//button[contains(@class,'buttonPrimary')][normalize-space()='Создать аккаунт']"
    )

    # --- Кнопка "Войти" (логин) ---
    ENTER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'homePage_modal__zSdUB')]"
        "//button[contains(@class,'buttonPrimary')][normalize-space()='Войти']"
    )
        # ===================== ЛОКАТОРЫ ДЛЯ ОБЪЯВЛЕНИЙ =====================

    # Кнопка "Разместить объявление" в шапке
    PLACE_AD_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Разместить объявление']"
    )

    # Заголовок модалки для неавторизованного пользователя:
    # "Чтобы разместить объявление, авторизуйтесь"
    PLACE_AD_LOGIN_MODAL_TITLE = (
        By.XPATH,
        "//*[contains(normalize-space(),'Чтобы разместить объявление, авторизуйтесь')]"
    )

        # Поле "Название" объявления
    # Берём либо input с плейсхолдером "Название", либо input сразу после label "Название"
    AD_TITLE_INPUT = (
        By.XPATH,
        "("
        "//input[contains(@placeholder,'Название')]"
        " | //input[contains(@placeholder,'название')]"
        " | //label[contains(normalize-space(),'Название')]/following::input[1]"
        ")[1]"
    )

    # Поле "Описание товара"
    # Аналогично: textarea с плейсхолдером "Описание" или рядом с label
    AD_DESCRIPTION_INPUT = (
        By.XPATH,
        "("
        "//textarea[contains(@placeholder,'Описание')]"
        " | //textarea[contains(@placeholder,'описание')]"
        " | //label[contains(normalize-space(),'Описание')]/following::textarea[1]"
        ")[1]"
    )
        
    # Поле "Стоимость" объявления
    AD_PRICE_INPUT = (
        By.XPATH,
        "("
        # input с плейсхолдером «Стоимость» / «стоимость» / «Цена» / «цена»
        "//input["
        "contains(@placeholder,'Стоимость')"
        " or contains(@placeholder,'стоимость')"
        " or contains(@placeholder,'Цена')"
        " or contains(@placeholder,'цена')"
        "]"
        " | "
        # input сразу после label с текстом про стоимость/цену
        "//label["
        "contains(normalize-space(),'Стоимость')"
        " or contains(normalize-space(),'стоимость')"
        " or contains(normalize-space(),'Цена')"
        " or contains(normalize-space(),'цена')"
        "]/following::input[1]"
        " | "
        # любой числовой инпут на форме
        "//input[@type='number' or @inputmode='decimal' or @inputmode='numeric']"
        ")[1]"
    )

        # Дропдаун "Категория" в форме создания объявления
    AD_CATEGORY_DROPDOWN = (
        By.XPATH,
        "("
        # 1) Обычный select с именем/айди category
        "//form//select[@name='category' or @id='category']"
        " | "
        # 2) Любой кликабельный элемент с name/id category
        "//form//*[@name='category' or @id='category'][self::select or self::div or self::button or self::input]"
        " | "
        # 3) Элемент сразу после label с текстом 'Категория'
        "//label[contains(normalize-space(),'Категория')]/following::*[self::select or self::div or self::button or self::input][1]"
        ")[1]"
    )
    # Общий локатор: первый пункт в открытом выпадающем списке
    AD_FIRST_OPTION = (
        By.XPATH,
        "("
        # 1) Нативный <select><option>
        "//select//option[not(@disabled)]"
        " | "
        # 2) Кастомные выпадашки: <ul>/<li> или <div> с опциями
        "//div[contains(@class,'menu') or contains(@class,'list') or contains(@class,'option') or contains(@class,'dropdown')]"
        "//*[self::li or self::div][not(contains(@class,'disabled'))]"
        ")[1]"
    )

    # Дропдаун "Город"
    AD_CITY_DROPDOWN = (
        By.XPATH,
        "//label[contains(normalize-space(),'Город')]/following::div[@role='combobox'][1]"
    )

    # Первая опция в открытом дропдауне (для категории/города)
    AD_CATEGORY_OPTION = (
        By.XPATH,
        "("
        "//select[contains(@name, 'category') or contains(@id, 'category')]"
        "/option[not(@disabled)][2]"
        ")[1]"
    )
    # Радиобаттон "Новый" в блоке "Состояние товара"
    AD_CONDITION_NEW = (
        By.XPATH,
        "//label[contains(normalize-space(),'Новый')]"
    )

    # Кнопка "Опубликовать"
    AD_PUBLISH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Опубликовать']"
    )

    # Заголовок объявления в блоке "Мои объявления"
    USER_AD_CARD_TITLE = (
        By.XPATH,
        "//section[contains(.,'Мои объявления')]//h3"
    )
    
    # Имя пользователя "User" в шапке рядом с аватаркой
    HEADER_USER_NAME = (
        By.XPATH,
        "//*[normalize-space()='User']"
    )
    
    # Кнопка "Выйти" в шапке после авторизации
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Выйти']"
    )

        # Дропдаун "Категория" в форме создания объявления
        # Дропдаун "Категория" в форме объявления
    AD_CATEGORY_DROPDOWN = (
        By.XPATH,
        "("
        # 1) Любой select рядом с текстом "Категория"
        "//*[contains(normalize-space(),'Категория')]/following::select[1]"
        " | "
        # 2) Любой элемент-виджет (div/button/input) рядом с текстом "Категория"
        "//*[contains(normalize-space(),'Категория')]/following::*[self::div or self::button or self::input][1]"
        ")[1]"
    )

    # Первая «живая» опция в открытом дропдауне категории
    AD_CATEGORY_OPTION = (
        By.XPATH,
        "("
        # 1) Обычный <select>
        "//select[contains(@name,'category') or contains(@id,'category')]"
        "/option[not(@disabled)][2]"
        " | "
        # 2) Кастомное выпадающее меню: div/li без disabled
        "//div[contains(@class,'menu') or contains(@class,'list') or contains(@class,'option') or contains(@class,'dropdown')]"
        "//*[self::div or self::li][not(contains(@class,'disabled'))][1]"
        ")[1]"
    )


    # Радиобаттон "Новый" в блоке "Состояние товара"
    AD_CONDITION_NEW = (
        By.XPATH,
        "//label[contains(normalize-space(),'Новый')]"
    )

    # Кнопка "Опубликовать"
    AD_PUBLISH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Опубликовать']"
    )

    # Заголовок объявления в блоке "Мои объявления"
    USER_AD_CARD_TITLE = (
        By.XPATH,
        "//section[contains(.,'Мои объявления')]//h3"
    )
