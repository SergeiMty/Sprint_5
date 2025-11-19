import random
import string

from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import TestDATA


class Helper:
    @staticmethod
    def random_email() -> str:
        """Генерирует рандомный email под заданный префикс и домен."""
        number = random.randint(1000, 9999)
        return f"{TestDATA.RANDOM_EMAIL_PREFIX}{number}@{TestDATA.RANDOM_EMAIL_DOMAIN}"
    
def login_as_existing_user(driver, wait):
    """Логин под заранее созданным пользователем из TestDATA."""
    # Нажать кнопку «Вход и регистрация»
    wait.until(
        EC.element_to_be_clickable(Locators.ENTER_AND_REGISTRATION_BUTTON)
    ).click()

    # Ждём появления формы авторизации
    wait.until(
        EC.visibility_of_element_located(Locators.LOGIN_FORM)
    )

    # Email
    email_input = wait.until(
        EC.visibility_of_element_located(Locators.EMAIL_INPUT)
    )
    email_input.clear()
    email_input.send_keys(TestDATA.LOGIN_EMAIL)

    # Пароль
    password_input = wait.until(
        EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(TestDATA.LOGIN_PASSWORD)

    # Кнопка «Войти»
    wait.until(
        EC.element_to_be_clickable(Locators.ENTER_BUTTON)
    ).click()

    # Убедиться, что модалка закрылась (успешный логин)
    wait.until(
        EC.invisibility_of_element_located(Locators.LOGIN_FORM)
    )
def generate_random_email():
    """Генерирует уникальный email для регистрации."""
    suffix = ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=6)
    )
    return f"{TestDATA.RANDOM_EMAIL_PREFIX}{suffix}@{TestDATA.RANDOM_EMAIL_DOMAIN}"

def open_registration_form(wait):
    """Открыть модалку регистрации: 'Вход и регистрация' -> 'Нет аккаунта'."""
    wait.until(
        EC.element_to_be_clickable(Locators.ENTER_AND_REGISTRATION_BUTTON)
    ).click()

    wait.until(
        EC.element_to_be_clickable(Locators.HAVE_NOT_ACCOUNT)
    ).click()

    wait.until(
        EC.visibility_of_element_located(Locators.REGISTRATION_FORM)
    )


def fill_passwords(wait):
    """Заполнить оба поля пароля одинаковым валидным значением."""
    password_input = wait.until(
        EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
    )
    password_input.clear()
    password_input.send_keys(TestDATA.PASSWORD)

    password_confirm_input = wait.until(
        EC.visibility_of_element_located(Locators.PASSWORD_CONFIRM_INPUT)
    )
    password_confirm_input.clear()
    password_confirm_input.send_keys(TestDATA.PASSWORD)


def assert_email_error(driver, wait):
    """Дождаться текста 'Ошибка' под email (проще всего — по page_source)."""
    wait.until(lambda d: TestDATA.ERROR_EMAIL in d.page_source)
    assert TestDATA.ERROR_EMAIL in driver.page_source
