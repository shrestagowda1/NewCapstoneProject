from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self, url):
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def find_all(self, by, locator):
        return self.wait.until(EC.presence_of_all_elements_located((by, locator)))

    def click(self, by, locator):
        el = self.find(by, locator)
        el.click()

    def type(self, by, locator, text):
        el = self.find(by, locator)
        el.clear()
        el.send_keys(text)

    def js_click(self, by, locator):
        el = self.find(by, locator)
        self.driver.execute_script('arguments[0].click();', el)

    def scroll_into_view(self, by, locator):
        el = self.find(by, locator)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', el)

    def execute_js(self, script, *args):
        return self.driver.execute_script(script, *args)

    def hover(self, by, locator):
        el = self.find(by, locator)
        ActionChains(self.driver).move_to_element(el).perform()

    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def switch_to_frame(self, by=None, locator=None, frame_reference=None):
        if frame_reference:
            self.driver.switch_to.frame(frame_reference)
        elif by and locator:
            el = self.find(by, locator)
            self.driver.switch_to.frame(el)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def take_screenshot(self, path):
        self.driver.save_screenshot(path)
