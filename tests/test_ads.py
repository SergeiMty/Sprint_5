from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import TestDATA
from helpers import login_as_existing_user


class TestAds:
    def test_create_ad_unauthorized_user(self, driver, wait):
        """Создание объявления неавторизованным пользователем."""

        # 1. Нажать кнопку «Разместить объявление».
        wait.until(
            EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON)
        ).click()

        # 2. Проверить: открылось модальное окно с текстом
        # «Чтобы разместить объявление, авторизуйтесь».
        title = wait.until(
            EC.visibility_of_element_located(
                Locators.PLACE_AD_LOGIN_MODAL_TITLE
            )
        )

        assert TestDATA.PLACE_AD_LOGIN_MODAL_TITLE in title.text

    def test_create_ad_authorized_user(self, driver, wait):
        """Создание объявления авторизованным пользователем."""

        # 1. Авторизоваться под заранее созданным пользователем.
        login_as_existing_user(driver, wait)

        # 2. Нажать кнопку «Разместить объявление».
        wait.until(
            EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON)
        ).click()

        # 3. Заполнить поле «Название».
        title_input = wait.until(
            EC.visibility_of_element_located(Locators.AD_TITLE_INPUT)
        )
        ad_title_text = "Тестовое объявление автотеста"
        title_input.clear()
        title_input.send_keys(ad_title_text)

        # 4. Заполнить поле «Описание товара».
        desc_input = wait.until(
            EC.visibility_of_element_located(Locators.AD_DESCRIPTION_INPUT)
        )
        desc_input.clear()
        desc_input.send_keys("Описание товара для автотеста")

        # 5. Заполнить поле «Стоимость» – только цифры.
        price_input = wait.until(
            EC.visibility_of_element_located(Locators.AD_PRICE_INPUT)
        )
        price_input.clear()
        price_input.send_keys("12345")

        # 6. Выбрать категорию из dropdown.
        category_dropdown = wait.until(
            EC.element_to_be_clickable(Locators.AD_CATEGORY_DROPDOWN)
        )
        category_dropdown.click()

        category_option = wait.until(
            EC.element_to_be_clickable(Locators.AD_CATEGORY_OPTION)
        )
        category_option.click()

        # 7. Отметить состояние «Новый».
        condition_new = wait.until(
            EC.element_to_be_clickable(Locators.AD_CONDITION_NEW)
        )
        condition_new.click()

        # 8. Нажать «Опубликовать».
        publish_button = wait.until(
            EC.element_to_be_clickable(Locators.AD_PUBLISH_BUTTON)
        )
        publish_button.click()

        # 9. Проверить, что объявление появилось в блоке «Мои объявления».
        card_title = wait.until(
            EC.visibility_of_element_located(Locators.USER_AD_CARD_TITLE)
        )
        assert ad_title_text in card_title.text
