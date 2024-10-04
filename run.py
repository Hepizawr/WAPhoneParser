import os.path
import sys
from pathlib import Path

from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable, \
    presence_of_element_located

from app.modules.browsers.defaultBrowser import get_default_browser
from app.modules.utils.cli_arguments import parser
from app.modules.utils.tools import get_translateY, get_next_chat, get_phone, get_element_or_wait
import config

if not (driver := get_default_browser()):
    sys.exit()

if profile := parser.parse_args().profile:
    driver.profile = os.path.expandvars(profile)

driver = driver.run(site="https://web.whatsapp.com")

contact_phone_numbers = set()
chat_list_area = get_element_or_wait(driver=driver, method=visibility_of_element_located,
                                     element_path=config.XPATH_CHAT_LIST_AREA, time=3600)
chats_count = int(chat_list_area.get_attribute("aria-rowcount"))
chats_length = int(chat_list_area.get_attribute("style").split('height: ')[1].split("px;")[0])

first_chat = True
while True:
    if first_chat:
        chat = get_element_or_wait(driver=driver, method=element_to_be_clickable, element_path=config.XPATH_CHAT(0))
        first_chat = False
    else:
        if (get_translateY(chat) + config.CHAT_LENGTH[1]) >= chats_length:
            break
        chat = get_next_chat(driver=driver, current_chat=chat)

    driver.execute_script("arguments[0].scrollIntoView(true);", chat)
    chat.click()

    dialog_area = get_element_or_wait(driver=driver, method=presence_of_element_located,
                                      element_path=config.XPATH_DIALOG_AREA, time=60)

    get_element_or_wait(driver=dialog_area, method=element_to_be_clickable,
                        element_path=config.XPATH_DIALOG_INFO_BUTTON, time=60).click()

    info_area = get_element_or_wait(driver=driver, method=presence_of_element_located,
                                    element_path=config.XPATH_INFO_AREA)

    if not (info_title := get_element_or_wait(driver=info_area, method=visibility_of_element_located,
                                              element_path=config.XPATH_INFO_TITLE).text):
        continue

    if info_title in config.CONTACT_TITLES:
        contact_phone_numbers.add(get_phone(info_area))
        Path("phone_numbers.txt").write_text('\n'.join(contact_phone_numbers))

driver.close()
