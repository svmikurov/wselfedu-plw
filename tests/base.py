"""
When developing a dough application, it uses class inheritance.
This module contains base classes for creating test runner classes.
"""

import unittest

import pytest
from playwright.sync_api import Page


class TestCasePage(unittest.TestCase):
    """The Playwright Pytest page fixture unittest TestCase class.

    A derived class from unittest.TestCase that adds Playwright Pytest
    page fixture.
    """

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Set up Playwright Pytest page fixture."""
        self.page = page
