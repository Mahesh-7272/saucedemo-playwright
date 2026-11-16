import re

from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_logout(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.logout()

    expect(login_page.login_button).to_be_visible()
    expect(page).not_to_have_url(re.compile("inventory.html"))