import allure
import pytest
from allure import severity_level
from pytest import fixture

from pages import Homepage, Header, Certification, PopularCourses


@allure.severity(severity_level.BLOCKER)
@allure.epic("Smoke тест")
@allure.feature("Загрузка страницы")
@allure.testcase("Задачи U1, U2")
@allure.story("Страница загружается успешно, основные элементы отображаются корректно")
@allure.title("Загрузка главной страницы")
@allure.description(
    """
    Цель: Проверка открытия страницы

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть домашнюю страницу
        2. Проверить значение "TITLE"
        3. Проверить корректность отображения элементов страницы

    Ожидаемый результат:
        - Значение "TITLE" соответствует главной странице
        - Элементы, уникальные для этой страницы, активны""")
def test_homepage(browser: fixture):
    homepage = Homepage(browser)
    homepage.open_homepage()
    homepage.check_page_title("Get Online Selenium Certification Course | Way2Automation")
    homepage.main_elements_are_active()
