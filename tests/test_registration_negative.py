# tests/test_registration_negative.py
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import TestDATA
from helpers import (
    open_registration_form,
    fill_passwords,
    assert_email_error,
)


class TestRegistrationNegative:
    """Негативные сценарии регистрации."""

    def test_registration_email_not_mask(self, driver, wait):
        """Регистрация пользователя с email не по маске."""
        open_registration_form(wait)

        # Email не по маске
        email_input = wait.until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(TestDATA.EMAIL_INVALID)

        fill_passwords(wait)

        # Пытаемся создать аккаунт
        wait.until(
            EC.element_to_be_clickable(Locators.REGISTRATION_SUBMIT_BUTTON)
        ).click()

        # Проверяем ошибку под email
        assert_email_error(driver, wait)

    def test_registration_existing_user(self, driver, wait):
        """Регистрация уже существующего пользователя."""
        open_registration_form(wait)

        # Email уже существующего юзера (создаём руками один раз)
        email_input = wait.until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(TestDATA.LOGIN_EMAIL)

        fill_passwords(wait)

        wait.until(
            EC.element_to_be_clickable(Locators.REGISTRATION_SUBMIT_BUTTON)
        ).click()

        # Ожидаем ту же самую "Ошибка" под email
        assert_email_error(driver, wait)
