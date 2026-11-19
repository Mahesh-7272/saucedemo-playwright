import re

import pytest
from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        ("", "Smith", "411062", "First Name is required"),
        ("John", "", "411062", "Last Name is required"),
        ("John", "Smith", "", "Postal Code is required"),
    ],
    ids=["missing first name", "missing last name", "missing postal code"],
)
def test_checkout_with_missing_details(
    page: Page, users, password, first_name, last_name, postal_code, expected_error
):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()
    login_page.login(users["standard"], password)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    cart_page.checkout()

    checkout_page.fill_details(first_name, last_name, postal_code)
    checkout_page.continue_to_overview()

    expect(checkout_page.error_message).to_contain_text(expected_error)
    expect(page).to_have_url(re.compile("checkout-step-one"))