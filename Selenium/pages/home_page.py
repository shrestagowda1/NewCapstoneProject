from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, 's')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    MENU_ITEMS = (By.CSS_SELECTOR, 'nav a')

    def search(self, term):
        self.type(*self.SEARCH_INPUT, text=term)
        self.click(*self.SEARCH_BUTTON)


