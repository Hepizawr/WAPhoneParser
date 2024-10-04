from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.webdriver import WebDriver

from app.modules.browsers.browser import Browser


class Edge(Browser):
    def __get_options(self) -> Options:
        options = Options()

        if self.profile:
            options.add_argument(f"user-data-dir={self.profile}")

        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")

        return options

    def run(self, site: str | None = None) -> WebDriver:
        options = self.__get_options()
        driver = webdriver.Edge(options=options)

        if site:
            driver.get(site)

        return driver
