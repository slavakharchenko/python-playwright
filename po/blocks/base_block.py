from playwright.sync_api import Page, Locator


class BaseBlock:
    def __init__(self, page: Page, root: Locator):
        self.page = page
        self.root = root
