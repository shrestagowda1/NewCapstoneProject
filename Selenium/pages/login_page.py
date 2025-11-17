from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    USER_INPUT = (By.ID, 'username')
    PASS_INPUT = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Login') or @type='submit']")
    ERROR_MSG = (By.CSS_SELECTOR, '.error')

    def login(self, username, password):
        self.type(*self.USER_INPUT, text=username)
        self.type(*self.PASS_INPUT, text=password)
        self.click(*self.LOGIN_BTN)

    def get_error(self):
        try:
            return self.find(*self.ERROR_MSG).text
        except Exception:
            return ''
