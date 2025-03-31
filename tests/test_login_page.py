import allure
import pytest
from allure import severity_level
from pytest import fixture

from data import LoginData
from pages import LoginPage


@allure.severity(severity_level.BLOCKER)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задачи U1, U2")
@allure.story("Страница загружается успешно, основные элементы отображаются корректно")
@allure.title("Авторизация на странице Login Page")
@allure.description(
    """
    Цель: Проверить поля ввода

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой
        2. Проверить наличие поля ввода "Username"
        3. Проверить наличие поля ввода "Password"
        4. Проверить наличие поля ввода "Username *"
        5. Проверить описание поля "Username"
        6. Проверить описание поля "Password"
        7. Проверить описание поля "Username *"

    Ожидаемый результат:
        - Поля отображаются
        - Описания соответствуют полям""")
def test_login_page(browser: fixture):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.check_username_field_label()
    login_page.check_password_field_label()
    login_page.check_username_desc_field_label()
