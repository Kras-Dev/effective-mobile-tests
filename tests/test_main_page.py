#tests/test_main_page.py
import time

import pytest
from conftest import browser
from pages.main_page import MainPage
import allure
from config.url_config import Links

class TestMainPage:
    # Параметризуем тест с различными значениями ссылок и ожидаемыми URL
    @pytest.mark.parametrize("link_name, expected_url", [
        ("logo", f"{Links.BASE_URL}#main"),
        ("about", f"{Links.BASE_URL}#about"),
        ("moreinfo", f"{Links.BASE_URL}#moreinfo"),
        ("cases", f"{Links.BASE_URL}#cases"),
        ("reviews", f"{Links.BASE_URL}#Reviews"),
        ("contacts", f"{Links.BASE_URL}#contacts"),
        ("specialists", f"{Links.BASE_URL}#specialists"),
    ])
    @allure.feature("Navigation Tests")
    def test_navigation(self, browser, link_name, expected_url):
        page = browser
        main_page = MainPage(page) # Передаем страницу в MainPage

        main_page.goto(Links.BASE_URL)
        # Проверяем, что мы на главной странице
        with allure.step("Navigate to main page"):
            assert main_page.get_url() == Links.BASE_URL, f"Expected URL {Links.BASE_URL}, but got {main_page.get_url()}"

        # Определяем словарь с действиями для клика по ссылкам на главной странице
        link_actions = {
            "logo": lambda: main_page.logo_link.click(), # Ссылка "Логотип"
            "about": lambda: main_page.about_link.click(), # Ссылка "О нас"
            "moreinfo": lambda: main_page.moreinfo_link.click(), # Ссылка "Услуги"
            "cases": lambda: main_page.cases_link.click(), # Ссылка "Проекты"
            "reviews": lambda: main_page.reviews_link.click(), # Ссылка "Отзывы"
            "contacts": lambda: main_page.contacts_link.click(), # Ссылка "Контакты"
            "specialists": lambda: main_page.specialists_link.click() # Ссылка "Выбрать специалиста"
        }

        # Выполняем действие клика
        if link_name in link_actions:
            with allure.step(f"Click on '{link_name.capitalize()}'"):
                link_actions[link_name]()

        # Проверяем, что текущий URL соответствует ожидаемому
        with allure.step("Check current URL"):
            assert main_page.get_url() == expected_url, f"Expected URL {expected_url}, but got {main_page.get_url()}"

        # time.sleep(2)