"""Login page testing module.

This module tests the login page.
"""

import os

from dotenv import load_dotenv
from playwright.sync_api import Page

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

    Tests the transition to the page, the username and password entry
    fields, and the title of the next page after a successful login.

    The login page is represented by the :ref:`LoginPage` class of page
    object model.

    Parameters
    ----------
    page : `Page`
        The Playwright Pytest fixture.
    """
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.test_title()

    # if the login is successful, then user redirects to the home page,
    # does not redirect otherwise
    login_page.login('wrong_user_name', 'wrong_user_pass')
    login_page.test_title()
    login_page.login(USER_NAME, USER_PASS)
    login_page.test_title('Домашняя страница')
