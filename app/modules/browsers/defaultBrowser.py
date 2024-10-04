import winreg

from app.modules.browsers.browser import Browser
from app.modules.browsers.chrome import Chrome
from app.modules.browsers.edge import Edge
from app.modules.browsers.firefox import Firefox
from app.modules.utils.tools import show_message_box_window


def get_default_browser() -> Browser | None:
    try:
        reg_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice"
        )
        browser_progid, _ = winreg.QueryValueEx(reg_key, "ProgId")

        if "Chrome" in browser_progid:
            return Chrome()
        elif "Firefox" in browser_progid:
            return Firefox()
        elif "Edge" in browser_progid:
            return Edge()
        else:
            show_message_box_window(title="Browser error", message=f"Unknown Browser (ProgId: {browser_progid})\n"
                                                                   f"Supported browsers: Google Chrome, Firefox, Microsoft Edge")
            return None

    except FileNotFoundError:
        show_message_box_window(title="Browser error", message="Default browser information not found")
        return None

    except Exception as e:
        show_message_box_window(title="Browser error", message=f"Error: {str(e)}")
        return None
