from playwright.sync_api import Page

from pages.base_page import TestingPage


class HomePage(TestingPage):
    """The home page representation class."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title = 'Домашняя страница'
