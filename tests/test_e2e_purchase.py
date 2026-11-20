import re

from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_complete_purchase(page: Page,users,password,customer):
    login_page=LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    complete_page = CheckoutCompletePage(page)

    #login
    login_page.open()
    login_page.login(users["standard"], password)

    #add 2 products
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    expect(inventory_page.cart_badge).to_have_text("2")

    # Check the cart
    inventory_page.open_cart()
    expect(cart_page.cart_items).to_have_count(2)

    # Enter customer details
    cart_page.checkout()
    checkout_page.fill_details(customer["first_name"], customer["last_name"], customer["postal_code"])
    checkout_page.continue_to_overview()
    expect(page).to_have_url(re.compile("checkout-step-two"))

    # Check the prices
    expect(checkout_page.item_total).to_have_text("Item total: $39.98")
    expect(checkout_page.tax).to_have_text("Tax: $3.20")
    expect(checkout_page.total).to_have_text("Total: $43.18")

    # Place the order
    checkout_page.finish()
    expect(complete_page.complete_header).to_have_text("Thank you for your order!")
    expect(inventory_page.cart_badge).not_to_be_visible()

    # Log out
    complete_page.back_home()
    inventory_page.logout()
    expect(login_page.login_button).to_be_visible()
