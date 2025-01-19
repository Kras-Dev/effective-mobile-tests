#pages/base_page.py
import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def get_url(self):
        return self.page.url

    def click_element(self, locator: str):
        self.page.click(locator)

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.page.screenshot(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )