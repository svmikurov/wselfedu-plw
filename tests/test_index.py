from playwright.sync_api import Page

from pages.index import IndexPage


def test_index_page(page: Page):
    """Test index page."""
    index_page = IndexPage(page)
    index_page.navigate()

    index_page.test_title()
