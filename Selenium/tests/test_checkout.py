import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_process(driver, base_url):
    # Go to login page
    driver.get(base_url + "/login")

    login = LoginPage(driver)
    login.login("testuser@example.com", "password123")

    # Go to cart
    cart = CartPage(driver)
    driver.get(base_url + "/cart")

    # Proceed to checkout
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)

    # Fill shipping details
    checkout.fill_shipping(
        name="John Doe",
        address="123 Test Street",
        city="New York",
        zipcode="10001"
    )

    # Place order
    checkout.place_order()

    # Verification
    assert "Order" in driver.title or "Success" in driver.page_source
