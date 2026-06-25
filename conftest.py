import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def handle_consent(page: Page):
    """Automatically dismiss the cookie consent popup on every test."""
    page.goto("https://automationexercise.com")

    try:
        consent_button = page.get_by_role("button", name="Consent")
        consent_button.wait_for(timeout=5000)
        consent_button.click()
    except Exception:
        pass  # Popup didn't appear, continue normally

    yield