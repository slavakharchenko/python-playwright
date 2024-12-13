from playwright.sync_api import Page
from .base_page import BasePage
from .blocks.search_blocks import SearchFormBlock


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.searchFormRoot = page.locator(
            "[data-test='LandingPageSearchForm']"
        )

        self.searchForm = SearchFormBlock(page, self.searchFormRoot)
