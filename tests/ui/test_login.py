import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

# Valid credentials — replace with an account you registered on the site
TEST_EMAIL = "email@testmail.com"
TEST_PASSWORD = "autopw1234"

class TestLogin:

    def test_login_with_valid_credentials(self, page: Page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(TEST_EMAIL, TEST_PASSWORD)
        assert login_page.is_logged_in(), "User should be logged in"

    def test_login_with_invalid_credentials(self, page: Page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("wrong@email.com", "wrongpassword")
        assert login_page.get_error_message(), "Error message should be visible"

