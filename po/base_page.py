import re
from playwright.sync_api import Page, expect


class BasePage:
    HOST = "https://www.kiwi.com"
    PATH = ""

    def __init__(self, page: Page):
        self.page = page
        self._accept_coockie = page.locator(
            "button[data-test='CookiesPopup-Accept']"
        )

    def create_url(self, language: str = "en"):
        return f"{self.HOST}/{language}/{self.PATH}"

    def acceptCoockie(self):
        if (self._accept_coockie.is_visible()): 
            self._accept_coockie.click()

    def check_url_includes(self, language: str = "en"):
        url = self.create_url(language)

        expect(self.page).to_have_url(re.compile(url))

        assert (
            url in self.page.url
        ), f"Expected URL: {url}, but got: {self.page.url}"

    def navigate(self, language: str = "en"):
        url = self.create_url(language)

        self.page.goto(url)
        expect(self.page).to_have_url(url)
