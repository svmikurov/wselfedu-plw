import os
import pathlib
import sys
from urllib.parse import urljoin

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, expect

load_dotenv()

HOST = os.getenv('HOST')
LOGIN_PATH = 'users/login/'
TEST_USER_NAME = os.getenv('TEST_USER_NAME')
TEST_USER_PASS = os.getenv('TEST_USER_PASS')
FILE_PATH = pathlib.Path(__file__).resolve().as_posix()
PATH_STATE = FILE_PATH + 'state.json'


def get_state(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(urljoin(HOST, LOGIN_PATH))

    page.locator('#id_username').fill(TEST_USER_NAME)
    page.locator('#id_password').fill(TEST_USER_PASS)
    page.get_by_test_id('login-button').click()

    page.context.storage_state(path=PATH_STATE)

    try:
        expect(page.get_by_text('Выйти')).to_be_visible()
    except AssertionError:
        print('Fatal')
    else:
        print('Success')


if __name__ == '__main__':
    with sync_playwright() as p:
        get_state(p)
