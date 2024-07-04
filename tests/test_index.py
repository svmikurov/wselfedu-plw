import os
from typing import Generator

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()

HOST = os.getenv('HOST')

@pytest.fixture(autouse=True)
def run_around_tests(page: Page) -> Generator[None, None, None]:
    """New browser page pytest-playwright fixture for a test."""
    page.goto(HOST)
    yield page


def test_page_status(page: Page) -> None:
    assert page.goto(page.url).ok


def test_page_title(page: Page) -> None:
    expect(page).to_have_title('Hello, Word!')
