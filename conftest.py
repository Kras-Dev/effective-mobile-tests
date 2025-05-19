#conftest.py

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='class')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(args=['--no-sandbox', '--disable-dev-shm-usage'],
                                             headless=True)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()