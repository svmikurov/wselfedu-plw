class IndexPage:
    """Representations of index page."""

    def __init__(self, page):
        self.page = page
        self.title = 'Домашняя страница'
        self.url = '127.0.0.1'

    def navigate(self):
        """Go to the testing page."""
        self.page.goto(self.testing_page_url)

    def test_title(self):
        """Test page title."""
        expect(page).to_have_title(self.title)
