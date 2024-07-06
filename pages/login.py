from playwright.sync_api import Page

from pages.base_page import TestingPage


class LoginPage(TestingPage):
    """The user login page class."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.path = '/users/login'
        self.title = 'Вход в приложение'
        self.user_name_input = page.get_by_placeholder('Имя пользователя')
        self.user_password_input = page.get_by_placeholder('Пароль')
        self.registration_button = page.get_by_role('button', name='Войти')

    def login(self, name: str, password: str) -> None:
        """Log in to the site."""
        self.user_name_input.fill(name)
        self.user_password_input.fill(password)
        self.registration_button.click()
