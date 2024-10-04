import ctypes

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import config


def get_translateY(chat: WebElement) -> int:
    return int(chat.get_attribute("style").split('translateY(')[1].split('px);')[0])


def get_next_chat(driver: WebDriver | WebElement, current_chat: WebElement) -> WebElement:
    while True:
        for i in config.CHAT_LENGTH:
            if chat := get_element_or_wait(driver=driver, method=element_to_be_clickable,
                                           element_path=config.XPATH_CHAT(translateY=get_translateY(current_chat) + i),
                                           time=1):
                return chat


def get_phone(area: WebElement) -> str:
    while True:
        try:
            name = WebDriverWait(area, 1).until(
                EC.visibility_of_element_located((By.XPATH, config.XPATH_INFO_NAME))).text
            if '+' in name:
                return name
        except:
            ...

        try:
            description = WebDriverWait(area, 1).until(
                EC.visibility_of_element_located((By.XPATH, config.XPATH_INFO_DESCRIPTION))).text
            if '+' in description:
                return description
        except:
            ...

        try:
            phone_area = WebDriverWait(area, 1).until(
                EC.presence_of_element_located((By.XPATH, config.XPATH_INFO_ABOUT_PHONE_AREA)))
            phone = phone_area.find_element(By.XPATH, config.XPATH_INFO_ABOUT_PHONE).text
            if '+' in phone:
                return phone
        except:
            ...


def get_element_or_wait(driver, method, element_path, time: float = 1.0) -> WebElement | None:
    try:
        return WebDriverWait(driver=driver, timeout=time).until(method((By.XPATH, element_path)))
    except:
        return


def show_message_box_window(title: str, message: str) -> None:
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)
