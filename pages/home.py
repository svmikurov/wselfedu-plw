from playwright.sync_api import Page

from pages.base import TestingPage


class HomePage(TestingPage):
    """The home page representation class."""

    title = 'Домашняя страница'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
