from selenium.webdriver.common.by import By
from .base_page import BasePage


class SearchPage(BasePage):
    PRODUCT_TITLES = (By.CSS_SELECTOR, '.product-title')
    ADD_TO_CART = (By.CSS_SELECTOR, '.add-to-cart')

    def add_first_product_to_cart(self):
        buttons = self.find_all(*self.ADD_TO_CART)
        if buttons:
            buttons[0].click()
