import re
from playwright.sync_api import Page, expect


def test_valid_login(page: Page):
    page.goto("/")
    page.get_by_test_id("username").fill("standard_user")
    page.get_by_test_id("password").fill("secret_sauce")
    page.get_by_test_id("login-button").click()

    expect(page).to_have_url(re.compile("inventory.html"))
    expect(page.get_by_test_id("title")).to_have_text("Products")


def test_locked_out_user(page: Page):
    page.goto("/")
    page.get_by_test_id("username").fill("locked_out_user")
    page.get_by_test_id("password").fill("secret_sauce")
    page.get_by_test_id("login-button").click()

    expect(page.get_by_test_id("error")).to_contain_text("locked out")
    expect(page).not_to_have_url(re.compile("inventory.html"))


def test_invalid_password(page: Page):
    page.goto("/")
    page.get_by_test_id("username").fill("standard_user")
    page.get_by_test_id("password").fill("wrong_password")
    page.get_by_test_id("login-button").click()

    expect(page.get_by_test_id("error")).to_contain_text("do not match")
    expect(page).not_to_have_url(re.compile("inventory.html"))


def test_empty_username(page: Page):
    page.goto("/")
    page.get_by_test_id("password").fill("secret_sauce")
    page.get_by_test_id("login-button").click()

    expect(page.get_by_test_id("error")).to_contain_text("Username is required")
    expect(page).not_to_have_url(re.compile("inventory.html"))
