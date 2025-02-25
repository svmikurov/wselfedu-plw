"""
User tests module.
"""

import os

from dotenv import load_dotenv
from playwright.sync_api import Page

from pages.home import HomePage
from pages import user_pages

load_dotenv()

USER_NAME = os.getenv('TEST_USER_NAME')
"""Login username.
"""
USER_PASS = os.getenv('TEST_USER_PASS')
"""User login password.
"""
TEMP_USER_NAME = 'temp-user'
"""User name for create and delete temp user.
"""
TEMP_USER_PASS = '1q2s3d4r'
"""Temp user password.
"""


def test_user_registration_page(page: Page) -> None:
    """Test the user registration page.

    Test:
        - page title;
        - fill form, by placeholders;
        - click submit;
        - redirect to login page if success registration, by title.

    Parameters
    ----------
    page : `Page`
        The Playwright Pytest fixture.
    """
    login_page = user_pages.LoginPage(page)
    reg_page = user_pages.RegistrationPage(page)

    reg_page.navigate()
    reg_page.test_title()
    reg_page.register(TEMP_USER_NAME, TEMP_USER_PASS)
    assert reg_page.current_title == login_page.title


def test_login_page(page: Page) -> None:
    """Test the login page.

    Test:
        - page title;
        - fill form, by placeholders;
        - no redirects if not success login, by title;
        - redirect to home page if success login, by title.

    Parameters
    ----------
    page : `Page`
        The Playwright Pytest fixture.
    """
    home_page = HomePage(page)
    login_page = user_pages.LoginPage(page)

    login_page.navigate()
    login_page.test_title()
    # if the login is successful, then user redirects to the home page,
    # does not redirect otherwise
    login_page.login('wrong_user_name', 'wrong_user_pass')
    login_page.test_title()
    login_page.login(USER_NAME, USER_PASS)
    assert login_page.current_title == home_page.title


def test_delete_user(page: Page):
    """Test delete user.

    Test:
        - click delete button;
        - click confirm button;
        - redirect to login page if success login, by title.

    Parameters
    ----------
    page : `Page`
        The Playwright Pytest fixture.
    """
    login_page = user_pages.LoginPage(page)
    delete_page = user_pages.UserDeletePage(page)

    # need user logged in
    delete_page.page.goto(login_page.url)
    delete_page.page.get_by_placeholder('Имя пользователя').fill(TEMP_USER_NAME)
    delete_page.page.get_by_placeholder('Пароль').fill(TEMP_USER_PASS)
    delete_page.page.get_by_role('button', name='Войти').click()

    delete_page.navigate()
    delete_page.delete_user()
    assert delete_page.current_title == login_page.title
