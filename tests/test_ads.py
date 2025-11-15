# tests/test_ads.py
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import TestDATA


class TestAds:
    # --- вспомогательный метод: логин заранее созданным пользователем ---
    def _login_as_existing_user(self, driver, wait):
        """Логин под заранее созданным пользователем."""

        # Кнопка "Вход и регистрация"
        wait.until(
            EC.element_to_be_clickable(Locators.ENTER_AND_REGISTRATION_BUTTON)
        ).click()

        # Ждём появления формы логина по полю Email
        email_input = wait.until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(TestDATA.EXISTING_EMAIL)

        # Пароль
        password_input = wait.until(
            EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(TestDATA.LOGIN_PASSWORD)

        # Жмём "Войти"
        wait.until(
            EC.element_to_be_clickable(Locators.ENTER_BUTTON)
        ).click()

        # Модалка должна исчезнуть
        wait.until(
            EC.invisibility_of_element_located(Locators.REGISTRATION_FORM)
        )

    #  1) Создание объявления неавторизованным пользователем ---
    def test_create_ad_unauthorized_user(self, driver, wait):
        """Создание объявления НЕавторизованным пользователем."""

        # Нажать кнопку «Разместить объявление».
        wait.until(
            EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON)
        ).click()

        # Проверить: отображается модальное окно с заголовком
        title = wait.until(
            EC.visibility_of_element_located(Locators.PLACE_AD_LOGIN_MODAL_TITLE)
        )
        assert "Чтобы разместить объявление, авторизуйтесь" in title.text

    #  2) Создание объявления авторизованным пользователем ---
    def test_create_ad_authorized_user(self, driver, wait):
        """Создание объявления авторизованным пользователем."""

        # 1. Авторизоваться под заранее созданным пользователем.
        self._login_as_existing_user(driver, wait)

        # 2. Нажать кнопку «Разместить объявление».
        wait.until(
            EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON)
        ).click()

        # 3. Заполнить все поля формы.

        # Название
        title_input = wait.until(
            EC.visibility_of_element_located(Locators.AD_TITLE_INPUT)
        )
        ad_title_text = "Тестовое объявление автотеста"
        title_input.clear()
        title_input.send_keys(ad_title_text)

        # Описание
        desc_input = wait.until(
            EC.visibility_of_element_located(Locators.AD_DESCRIPTION_INPUT)
        )
        desc_input.clear()
        desc_input.send_keys("Описание товара для автотеста")

        # Стоимость – чисто цифры
        price_input = wait.until(
            EC.visibility_of_element_located(Locators.AD_PRICE_INPUT)
        )
        price_input.clear()
        price_input.send_keys("12345")

        # Категория
        wait.until(
            EC.element_to_be_clickable(Locators.AD_CATEGORY_DROPDOWN)
        ).click()
        wait.until(
            EC.element_to_be_clickable(Locators.AD_FIRST_OPTION)
        ).click()

        # Город
        wait.until(
            EC.element_to_be_clickable(Locators.AD_CITY_DROPDOWN)
        ).click()
        wait.until(
            EC.element_to_be_clickable(Locators.AD_FIRST_OPTION)
        ).click()

        # Состояние товара — выбираем "Новый"
        wait.until(
            EC.element_to_be_clickable(Locators.AD_CONDITION_NEW)
        ).click()

        # 4. Нажать кнопку «Опубликовать».
        wait.until(
            EC.element_to_be_clickable(Locators.AD_PUBLISH_BUTTON)
        ).click()

        # 5. Перейти в профиль пользователя.
        wait.until(
            EC.element_to_be_clickable(Locators.USER_PROFILE_LINK)
        ).click()

        # 6. Проверить: в блоке «Мои объявления» отображается созданное объявление.
        user_ad_title = wait.until(
            EC.visibility_of_element_located(Locators.USER_AD_CARD_TITLE)
        )
        assert ad_title_text in user_ad_title.text
