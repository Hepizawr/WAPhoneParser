from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from app.modules.browsers.browser import Browser


class Chrome(Browser):
    def __get_options(self) -> Options:
        options = Options()

        if self.profile:
            options.add_argument(f"user-data-dir={self.profile}")

        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")

        return options

    def run(self, site: str | None = None) -> WebDriver:
        options = self.__get_options()
        driver = webdriver.Chrome(options=options)

        if site:
            driver.get(site)

        return driver
