# tests/test_registration_positive.py
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import TestDATA
from helpers import Helper


class TestRegistration:
    def test_registration_positive(self, driver, wait):
        """Регистрация нового пользователя с рандомным email."""

        # 1. Открываем модалку логина
        wait.until(
            EC.element_to_be_clickable(Locators.ENTER_AND_REGISTRATION_BUTTON)
        ).click()

        # 2. Жмём "Нет аккаунта"
        wait.until(
            EC.element_to_be_clickable(Locators.HAVE_NOT_ACCOUNT)
        ).click()

        # 3. Ждём появления формы регистрации
        wait.until(
            EC.visibility_of_element_located(Locators.REGISTRATION_FORM)
        )

        # 4. Email — берём случайный
        email = Helper.random_email()
        email_input = wait.until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(email)

        # 5. Пароль
        password_input = wait.until(
            EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(TestDATA.PASSWORD)

        # 6. Повтор пароля
        password_confirm_input = wait.until(
            EC.visibility_of_element_located(Locators.PASSWORD_CONFIRM_INPUT)
        )
        password_confirm_input.clear()
        password_confirm_input.send_keys(TestDATA.PASSWORD)

        # 7. Жмём "Создать аккаунт"
        wait.until(
            EC.element_to_be_clickable(Locators.REGISTRATION_SUBMIT_BUTTON)
        ).click()

        # 8. Проверяем, что форма закрылась (значит, регистрация прошла)
        wait.until(
            EC.invisibility_of_element_located(Locators.REGISTRATION_FORM)
        )
