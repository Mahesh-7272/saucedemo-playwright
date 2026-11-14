import re

from playwright.sync_api import Page, expect


def test_valid_login(page:Page):
    page.goto("/")
    page.get_by_test_id("username").fill("standard_user")
    page.get_by_test_id("password").fill("secret_sauce")
    page.get_by_test_id("login-button").click()

    expect(page).to_have_url(re.compile("inventory.html"))
    expect(page.get_by_test_id("title")).to_have_text("Products")