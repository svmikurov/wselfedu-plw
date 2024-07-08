"""Login page testing module.

This module tests the login page.
"""

import os

from dotenv import load_dotenv
from playwright.sync_api import Page

from pages.home import HomePage
from pages.login import LoginPage

load_dotenv()

USER_NAME = os.getenv('TEST_USER_NAME')
"""Login username.
"""
USER_PASS = os.getenv('TEST_USER_PASS')
"""User login password.
"""


def test_login_page(page: Page) -> None:
    """Test the login page.

    Test:
        - load login page
        - login with wrong user data
        - no redirects if not success login
        - login
        - redirect to home page if success login

    Parameters
    ----------
    page : `Page`
        The Playwright Pytest fixture.
    """
    test_page = LoginPage(page)
    test_page.navigate()
    test_page.test_title()

    # if the login is successful, then user redirects to the home page,
    # does not redirect otherwise
    test_page.login('wrong_user_name', 'wrong_user_pass')
    test_page.test_title()
    test_page.login(USER_NAME, USER_PASS)
    assert test_page.title == HomePage.title
