from playwright.sync_api import Page

from pages.base import TestingPage


class CreateWordPage(TestingPage):
    """Add word to english dictionary class."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.path = '/english/word/create'
        self.title = 'Добавить слово в словарь'
        self.english_word_input = page.get_by_label('Слово на английском')
        self.russian_word_input = page.get_by_label('Слово на русском')
        self.submit_button = page.get_by_role('button', name='Сохранить')

    def create_word(self):
        """Test add word to english dictionary."""
        self.english_word_input.fill('карандаш')
        self.english_word_input.fill('a pencil')
        self.submit_button.click()
