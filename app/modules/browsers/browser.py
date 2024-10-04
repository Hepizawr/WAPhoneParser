from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver


class Browser(ABC):
    def __init__(
            self,
            profile: str | None = None
    ):
        self.profile = profile

    @abstractmethod
    def run(self, site: str | None = None) -> WebDriver:
        pass
