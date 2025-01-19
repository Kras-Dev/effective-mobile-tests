#pages/main_page.py
from playwright.sync_api import Page

from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logo_link = page.locator('div.tn-atom:not([style]) a[href="#main"]')  # Ссылка "Логотип"
        self.about_link = page.locator('a[href="#about"].tn-atom')  # Ссылка "О нас"
        self.moreinfo_link = page.locator('a[href="#moreinfo"].tn-atom').filter(has_text="[ Услуги ]")  # Ссылка "Услуги"
        self.cases_link = page.locator('a[href="#cases"].tn-atom')  # Ссылка "Проекты"
        self.reviews_link = page.locator('a[href="#Reviews"].tn-atom')  # Ссылка "Отзывы"
        self.contacts_link = page.locator('a[href="#contacts"].tn-atom').filter(has_text="[ Контакты ]")  # Ссылка "Контакты"
        self.specialists_link = page.locator('a[href="#specialists"]')  # Ссылка "Выбрать специалиста"


