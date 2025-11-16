class Urls:
    DOSKA_URL = "https://qa-desk.stand.praktikum-services.ru/"


class TestDATA:
    # Пароль, который используем и в регистрации, и в логине
    PASSWORD = "Qwerty123!"

    # email НЕ по маске для негативного кейса
    EMAIL_INVALID = "autotester128example.com"

    # --- Настройки для генерации случайного email (позитивная регистрация) ---
    RANDOM_EMAIL_PREFIX = "autotest_"
    RANDOM_EMAIL_DOMAIN = "mail.ru"

    # --- Ожидаемые сообщения об ошибках ---
    ERROR_EMAIL = "Ошибка"
    ERROR_LOGIN = "Логин или пароль неверны"

    # --- Данные для логина (существующий пользователь) ---
    # ЭТОГО юзера один раз создай руками через форму регистрации
    LOGIN_EMAIL = "autotest_login@example.com"
    LOGIN_PASSWORD = PASSWORD

    # --- Алиасы для тестов, где используется EXISTING_* ---
    # чтобы не переписывать уже написанные тесты
    EXISTING_EMAIL = LOGIN_EMAIL
    EXISTING_PASSWORD = LOGIN_PASSWORD
    # Ожидаемый текст для модалки размещения объявления
    PLACE_AD_LOGIN_MODAL_TITLE = "Чтобы разместить объявление, авторизуйтесь"

    # Имя пользователя, которое отображается в шапке
    USER_NAME = "User"