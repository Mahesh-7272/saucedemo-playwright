import re

from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_item_to_cart(page: Page, users, password):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login(users["standard"], password)

    inventory_page.add_to_cart("sauce-labs-backpack")

    expect(inventory_page.cart_badge).to_have_text("1")


def test_remove_item_from_cart_page(page: Page, users, password):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login(users["standard"], password)

    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    expect(page).to_have_url(re.compile("cart.html"))

    cart_page.remove_item("sauce-labs-backpack")

    expect(inventory_page.cart_badge).not_to_be_visible()