from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.webdriver import WebDriver

from app.modules.browsers.browser import Browser


class Firefox(Browser):
    def __get_options(self) -> FirefoxOptions:
        options = FirefoxOptions()

        if self.profile:
            options.profile = FirefoxProfile(profile_directory=self.profile)

        options.set_preference("dom.webnotifications.enabled", False)
        options.set_preference("extensions.enabled", False)

        return options

    def run(self, site: str | None = None) -> WebDriver:
        options = self.__get_options()
        driver = webdriver.Firefox(options=options)

        if site:
            driver.get(site)

        return driver
