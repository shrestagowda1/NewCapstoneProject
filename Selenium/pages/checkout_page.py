from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    NAME = (By.ID, 'name')
    ADDRESS = (By.ID, 'address')
    CITY = (By.ID, 'city')
    ZIP = (By.ID, 'zipcode')
    PLACE_ORDER = (By.XPATH, "//button[contains(text(),'Place Order')]")

    def fill_shipping(self, name, address, city, zipcode):
        self.type(*self.NAME, text=name)
        self.type(*self.ADDRESS, text=address)
        self.type(*self.CITY, text=city)
        self.type(*self.ZIP, text=zipcode)

    def place_order(self):
        self.click(*self.PLACE_ORDER)
