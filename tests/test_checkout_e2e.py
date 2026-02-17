from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_complete_flow(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Login
    login.open()
    login.login("standard_user", "secret_sauce")

    # Add product
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    # Cart → Checkout
    cart.click_checkout()

    # Checkout Steps
    checkout.fill_customer_info()
    checkout.finish_checkout()

    # Validation
    assert checkout.get_success_message() == "Thank you for your order!"
