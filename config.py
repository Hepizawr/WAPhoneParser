XPATH_CHAT_LIST_AREA = "//div[@class='x1y332i5 x1n2onr6 x6ikm8r x10wlt62']"


def XPATH_CHAT(translateY: int | None = None):
    if not translateY is None:
        return f"//*[contains(@style, 'translateY({translateY}px)')]"
    return f"//*[contains(@style, 'translateY')]"


XPATH_DIALOG_AREA = "//div[@class='_ajx_']"
XPATH_DIALOG_INFO_BUTTON = ".//div[@class='_amie']"

XPATH_INFO_AREA = "//div[@class='_aigv _aig- _aohg _arpo']"
XPATH_INFO_TITLE = ".//h1[@class='x1qlqyl8 x1pd3egz xcgk4ki']"
XPATH_INFO_NAME = ".//span[@class='x1rg5ohu x13faqbe _ao3e selectable-text copyable-text']"
XPATH_INFO_DESCRIPTION = ".//span[@class='x1jchvi3 x1fcty0u x40yjcy']"

XPATH_INFO_ABOUT_PHONE_AREA = ".//div[@class='xkhd6sd  _ajxt']"
XPATH_INFO_ABOUT_PHONE = ".//span[@class='x1lkfr7t xdbd6k5 x1fcty0u xw2npq5']"

CONTACT_TITLES = ("Contact info", "Данные контакта", "Інформація про контакт")
CHAT_LENGTH = (72, 91)
