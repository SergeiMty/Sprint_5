# tests/test_login.py
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import TestDATA


class TestLogin:
    def test_login_user(self, driver, wait):
        """
        Login пользователя:
        - нажать 'Вход и регистрация',
        - ввести email/пароль заранее созданного юзера,
        - нажать 'Войти',
        - проверить, что модалка закрылась и нет текста об ошибке логина.
        """

        # 1. Открываем модалку логина
        wait.until(
            EC.element_to_be_clickable(Locators.ENTER_AND_REGISTRATION_BUTTON)
        ).click()

        # 2. Ждём, пока форма авторизации станет видимой
        wait.until(
            EC.visibility_of_element_located(Locators.REGISTRATION_FORM)
        )

        # 3. Email
        email_input = wait.until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(TestDATA.LOGIN_EMAIL)

        # 4. Пароль
        password_input = wait.until(
            EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(TestDATA.LOGIN_PASSWORD)

        # 5. Жмём "Войти"
        wait.until(
            EC.element_to_be_clickable(Locators.ENTER_BUTTON)
        ).click()

        # 6. Модалка должна исчезнуть — успешный логин
        wait.until(
            EC.invisibility_of_element_located(Locators.REGISTRATION_FORM)
        )

        # 7. На странице не должно быть текста об ошибке логина
        assert TestDATA.ERROR_LOGIN not in driver.page_source
