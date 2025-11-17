import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_search_and_add_to_cart(driver, base_url):
    home = HomePage(driver)
    home.open(base_url)

    # Step 1: Search for a product
    home.search("laptop")

    search = SearchPage(driver)
    search.add_first_product_to_cart()

    # Step 2: Validate the product was added
    cart = CartPage(driver)
    driver.get(base_url + "/cart")

    checkout_btn = cart.find(*cart.CHECKOUT_BTN)
    assert checkout_btn.is_displayed(), "Checkout button not visible – Product not added."
