"""
User tests module.
"""

import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
from psycopg2.extras import NamedTupleCursor

from db_con import db
from pages.home import HomePage
from pages.user import LoginPage, UserDeletePage, CreateUserPage
from tests.base import TestCasePage

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
"""Connect data for connect to Postres database.
"""
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


class TestCrudUserPage(TestCasePage):
    """CRUD user pages class."""

    def tearDown(self):
        """Tear down after each method test.

        Truncate cascade the users database table.
        """
        connection = db.connect(DATABASE_URL)
        db.truncate_user_table(connection)
        db.close(connection)

    def test_create_user_page(self):
        """Test the user registration page."""
        page = CreateUserPage(self.page)
        page.navigate()
        page.create_user(TEMP_USER_NAME, TEMP_USER_PASS)

        # redirect to home page after successful user creation
        assert page.current_title == LoginPage.title

        # an entry with the username should appear
        # in the "users_usermodel" table of the database
        connection = db.connect(DATABASE_URL)
        has_db_user = self.check_has_db_user(connection, TEMP_USER_NAME)
        db.close(connection)
        assert has_db_user is True

    @staticmethod
    def check_has_db_user(connection, user_namer):
        """Check if there is a registered user in the database."""
        with connection.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute(
                '''
                SELECT username
                FROM users_usermodel
                WHERE username = %s
                ''',
                (user_namer,)
            )
            check = curs.fetchone()
        return True if check else False


@pytest.mark.skip
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
    login_page = LoginPage(page)
    reg_page = CreateUserPage(page)

    reg_page.navigate()
    reg_page.test_title()
    reg_page.register(TEMP_USER_NAME, TEMP_USER_PASS)
    assert reg_page.current_title == login_page.title


@pytest.mark.skip('There will be refactoring')
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
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.test_title()
    # if the login is successful, then user redirects to the home page,
    # does not redirect otherwise
    login_page.login('wrong_user_name', 'wrong_user_pass')
    login_page.test_title()
    login_page.login(USER_NAME, USER_PASS)
    assert login_page.current_title == home_page.title


@pytest.mark.skip('There will be refactoring')
def test_delete_user(page: Page) -> None:
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
    login_page = LoginPage(page)
    delete_page = UserDeletePage(page)

    # need user logged in
    delete_page.page.goto(login_page.url)
    delete_page.page.get_by_placeholder('Имя пользователя').fill(TEMP_USER_NAME)
    delete_page.page.get_by_placeholder('Пароль').fill(TEMP_USER_PASS)
    delete_page.page.get_by_role('button', name='Войти').click()
    home_page = HomePage(page)
    assert login_page.current_title == home_page.title

    delete_page.navigate()
    delete_page.delete_user()
    assert delete_page.current_title == login_page.title
