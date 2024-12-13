from playwright.sync_api import Page, expect
from .base_page import BasePage


class ResultPage(BasePage):
    PATH = "search/results"

    def __init__(self, page: Page):
        super().__init__(page)
        self._resultCards = page.locator(
            "[data-test='ResultCardSectorWrapper']"
        )

    def checkResultIsNotEmpty(self):
        expect(self._resultCards, "Result card is empty").not_to_have_count(0)
        print(f"Result has {self._resultCards.count} cards")
