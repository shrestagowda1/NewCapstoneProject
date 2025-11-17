from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from .config_reader import config


class DriverFactory:
    @staticmethod
    def create_driver():
        browser = config.get('browser', 'chrome')
        headless = config.get('headless', False)

        if browser.lower() == 'chrome':
            options = Options()

            if headless:
                options.add_argument('--headless=new')
                options.add_argument('--disable-gpu')

            options.add_argument('--start-maximized')

            drv = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        else:
            raise Exception("Only Chrome browser is supported in this framework.")

        # Additional driver settings
        drv.implicitly_wait(config.get('implicit_wait', 5))
        drv.set_page_load_timeout(config.get('page_load_timeout', 30))

        return drv
