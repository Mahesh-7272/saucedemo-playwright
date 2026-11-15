import re

from playwright.sync_api import Page, expect


def test_logout(page: Page):
    page.goto("/")
    page.get_by_test_id("username").fill("standard_user")
    page.get_by_test_id("password").fill("secret_sauce")
    page.get_by_test_id("login-button").click()

    page.get_by_role("button", name="Open Menu").click()
    page.get_by_test_id("logout-sidebar-link").click()

    expect(page.get_by_test_id("login-button")).to_be_visible()
    expect(page).not_to_have_url(re.compile("inventory.html"))
