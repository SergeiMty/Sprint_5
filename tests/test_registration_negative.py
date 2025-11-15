# tests/test_registration_negative.py
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import TestDATA
from helpers import Helper  # пока не используется, но пусть будет — на будущее


class TestRegistrationNegative:
    """Негативные сценарии регистрации."""

    # --- Вспомогательные методы ---

    def _open_registration_form(self, wait):
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

    def _fill_passwords(self, wait):
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

    def _assert_email_error(self, driver, wait):
        """Дождаться текста 'Ошибка' под email (проще всего — по page_source)."""
        wait.until(lambda d: TestDATA.ERROR_EMAIL in d.page_source)
        assert TestDATA.ERROR_EMAIL in driver.page_source

    # --- Тесты ---

    def test_registration_email_not_mask(self, driver, wait):
        """Регистрация пользователя с email не по маске."""
        self._open_registration_form(wait)

        # Email не по маске
        email_input = wait.until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(TestDATA.EMAIL_INVALID)

        self._fill_passwords(wait)

        # Пытаемся создать аккаунт
        wait.until(
            EC.element_to_be_clickable(Locators.REGISTRATION_SUBMIT_BUTTON)
        ).click()

        # Проверяем ошибку под email
        self._assert_email_error(driver, wait)

    def test_registration_existing_user(self, driver, wait):
        """Регистрация уже существующего пользователя."""
        self._open_registration_form(wait)

        # Email уже существующего юзера (создаём руками один раз)
        email_input = wait.until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(TestDATA.LOGIN_EMAIL)

        self._fill_passwords(wait)

        wait.until(
            EC.element_to_be_clickable(Locators.REGISTRATION_SUBMIT_BUTTON)
        ).click()

        # Ожидаем ту же самую "Ошибка" под email
        self._assert_email_error(driver, wait)
