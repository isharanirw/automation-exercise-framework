import pytest
import uuid
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


class TestSignup:

    def test_register_new_user(self, page: Page):
        # Use unique email each run so it never clashes
        unique_email = f"testuser_{uuid.uuid4().hex[:8]}@example.com"

        login_page = LoginPage(page)
        signup_page = SignupPage(page)

        login_page.navigate()
        signup_page.enter_name_and_email("Test User", unique_email)
        signup_page.fill_account_details(
            password="Test@1234",
            first_name="Test",
            last_name="User",
            address="123 Test Street",
            state="Ontario",
            city="Toronto",
            zipcode="M5H2N2",
            mobile="0771234567"
        )

        assert signup_page.is_account_created(), "Account Created message should be visible"
        signup_page.continue_after_signup()
        assert signup_page.is_logged_in(), "User should be logged in after registration"

    def test_register_with_existing_email(self, page: Page):
        login_page = LoginPage(page)
        signup_page = SignupPage(page)

        # Use an email you already registered
        login_page.navigate()
        signup_page.enter_name_and_email("Test User", "email@testmail.com")

        assert signup_page.is_email_already_exists(), "Email already exists error should be visible"