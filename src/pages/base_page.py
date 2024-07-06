import os

from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()

HOST = os.getenv('HOST')


class BasePage:
    """Base page class."""

    host = HOST

    def __init__(self, page: Page) -> None:
        self.page = page
        self.path = ''

    @property
    def url(self) -> str:
        """Page url."""
        return self.host + self.path

    def navigate(self) -> None:
        """Go to page url."""
        self.page.goto(self.url)


class CommonTests:
    """Common page tests class."""

    page: Page
    title: str

    def test_title(self, expected_title=None) -> bool:
        """Test page title."""
        title = expected_title or self.title
        return expect(self.page).to_have_title(title)


class TestingPage(BasePage, CommonTests):
    """Base testing page with general tests."""
