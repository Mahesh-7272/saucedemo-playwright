import re

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(re.compile("inventory.html"))
    expect(inventory_page.title).to_have_text("Products")


def test_locked_out_user(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message).to_contain_text("locked out")
    expect(page).not_to_have_url(re.compile("inventory.html"))


def test_invalid_password(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")

    expect(login_page.error_message).to_contain_text("do not match")
    expect(page).not_to_have_url(re.compile("inventory.html"))


def test_empty_username(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "secret_sauce")

    expect(login_page.error_message).to_contain_text("Username is required")
    expect(page).not_to_have_url(re.compile("inventory.html"))
