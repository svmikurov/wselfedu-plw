from playwright.sync_api import Page

from pages.home import HomePage


def test_home_page(page: Page):
    """Test home page."""
    home_page = HomePage(page)
    home_page.navigate()

    home_page.test_title()
