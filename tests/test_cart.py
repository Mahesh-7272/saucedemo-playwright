import re

from playwright.sync_api import Page, expect


def test_add_item_to_cart(page: Page):
    page.goto("/")
    page.get_by_test_id("username").fill("standard_user")
    page.get_by_test_id("password").fill("secret_sauce")
    page.get_by_test_id("login-button").click()

    page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()

    expect(page.get_by_test_id("shopping-cart-badge")).to_have_text("1")


def test_remove_item_from_cart_page(page: Page):
    page.goto("/")
    page.get_by_test_id("username").fill("standard_user")
    page.get_by_test_id("password").fill("secret_sauce")
    page.get_by_test_id("login-button").click()

    page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()
    page.get_by_test_id("shopping-cart-link").click()
    expect(page).to_have_url(re.compile("cart.html"))

    page.get_by_test_id("remove-sauce-labs-backpack").click()

    expect(page.get_by_test_id("shopping-cart-badge")).not_to_be_visible()