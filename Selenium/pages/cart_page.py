from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    # class-level locator MUST be indented
    CHECKOUT_BTN = (By.LINK_TEXT, 'Checkout')

    def proceed_to_checkout(self):
        # method body MUST be indented
        self.click(*self.CHECKOUT_BTN)
