"""
User pages module.
"""

from playwright.sync_api import Page

from pages.base import TestingPage


class CreateUserPage(TestingPage):
    """The user registration page class."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = '/users/registration/'
        self.title = 'Регистрация пользователя'
        self.user_name_input = page.get_by_placeholder('Имя пользователя')
        self.user_password1_input = page.get_by_placeholder('Пароль')
        self.user_password2_input = page.get_by_placeholder(
            'Подтверждение пароля',
        )
        self.submit_button = page.get_by_role(
            'button', name='Зарегистрироваться',
        )

    def create_user(self, user_name: str, user_pass: str) -> None:
        """Register a new user.

        Fills out the user registration form. Clicks on the submit form
        button.

        Parameters
        ----------
        user_name : `str`
            Login of the registered user.
        user_pass : `str`
            Password of the registered user.
        """
        self.user_name_input.fill(user_name)
        self.user_password1_input.fill(user_pass)
        self.user_password2_input.fill(user_pass)
        self.submit_button.click()


class LoginPage(TestingPage):
    """The user login page class."""

    title = 'Вход в приложение'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.path = '/users/login'
        self.user_name_input = page.get_by_placeholder('Имя пользователя')
        self.user_password_input = page.get_by_placeholder('Пароль')
        self.registration_button = page.get_by_role('button', name='Войти')

    def login(self, name: str, password: str) -> None:
        """Log in to the site."""
        self.user_name_input.fill(name)
        self.user_password_input.fill(password)
        self.registration_button.click()


class UserDeletePage(TestingPage):
    """User delete page class."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.title = 'Удаление пользователя'
        self.account_link_locator = page.get_by_test_id("account-link")
        self.delete_button_locator = page.get_by_role("link", name="Удалить")
        self.confirm_locator = page.get_by_role("button", name="Удалить")

    def navigate(self):
        """Navigate to user account."""
        account_path = self.account_link_locator.get_attribute('href')
        self.page.goto(self.host + account_path)

    def delete_user(self):
        """Delete user."""
        self.delete_button_locator.click()
        self.confirm_locator.click()
