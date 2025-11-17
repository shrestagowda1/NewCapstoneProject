from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    TITLE = (By.CSS_SELECTOR, 'h1')
    ADD_TO_CART = (By.ID, 'add-to-cart')

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)
