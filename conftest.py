import pytest
from playwright.sync_api import Page


def block_ads(page):
    """Block ad network requests before they load."""
    page.route("**/*", lambda route: (
        route.abort()
        if any(domain in route.request.url for domain in [
            "googlesyndication.com",
            "doubleclick.net",
            "googletagmanager.com",
            "googletagservices.com",
            "google-analytics.com",
            "adservice.google.com",
            "pagead2.googlesyndication.com",
        ])
        else route.continue_()
    ))


def dismiss_overlays(page):
    """Dismiss any remaining overlays after page load."""
    # Cookie consent
    try:
        consent = page.get_by_role("button", name="Consent")
        consent.wait_for(timeout=2000)
        if consent.is_visible():
            consent.click()
            page.wait_for_timeout(300)
    except Exception:
        pass

    # Close button ads
    try:
        close = page.locator('a:has-text("Close"), button:has-text("Close")')
        if close.first.is_visible(timeout=2000):
            close.first.click()
            page.wait_for_timeout(300)
    except Exception:
        pass


@pytest.fixture(autouse=True)
def handle_consent(page: Page):
    """Block ads and dismiss overlays before every test."""
    block_ads(page)
    page.goto("https://automationexercise.com")
    dismiss_overlays(page)
    yield