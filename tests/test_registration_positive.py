from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_random_email

from locators import Locators
from data import TestDATA


class TestRegistration:

    def test_registration_positive(self, driver, wait):
        """Регистрация нового пользователя с рандомным email."""

        # 1. Открываем модалку логина
        wait.until(
            EC.element_to_be_clickable(Locators.ENTER_AND_REGISTRATION_BUTTON)
        ).click()

        # 2. Переходим на форму регистрации
        wait.until(
            EC.element_to_be_clickable(Locators.HAVE_NOT_ACCOUNT)
        ).click()

        # 3. Ждём появления формы регистрации
        wait.until(
            EC.visibility_of_element_located(Locators.REGISTRATION_FORM)
        )

        # 4. Заполняем email, пароль и подтверждение пароля
        email_input = wait.until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.clear()
        random_email = generate_random_email()
        email_input.send_keys(random_email)

        password_input = wait.until(
            EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(TestDATA.PASSWORD)

        repeat_input = wait.until(
            EC.visibility_of_element_located(Locators.PASSWORD_CONFIRM_INPUT)
        )
        repeat_input.clear()
        repeat_input.send_keys(TestDATA.PASSWORD)

        # 5. Жмём кнопку регистрации
        wait.until(
            EC.element_to_be_clickable(Locators.REGISTRATION_SUBMIT_BUTTON)
        ).click()

        # 6. Форма должна исчезнуть
        wait.until(
            EC.invisibility_of_element_located(Locators.REGISTRATION_FORM)
        )

        # 7. Проверяем, что пользователь залогинен:
        #    в шапке появилась кнопка "Выйти"
        logout_button = wait.until(
            EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)
        )
        assert logout_button.is_displayed()

        # 8. На странице где-то присутствует имя User
        assert "User" in driver.page_source
