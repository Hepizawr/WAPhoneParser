import argparse

parser = argparse.ArgumentParser(
    description=(
        "This program parses phone numbers from active WhatsApp chats "
        "using its web version. The browser in which the parsing occurs "
        "is determined based on the default browser set in the Windows system. "
        "Supported browsers include Chrome, Firefox, and Edge. "
        "The program will automatically open the web version of WhatsApp and extract "
        "phone numbers from the available chats. All found phone numbers will be saved "
        "in a file named 'phone_numbers.txt', which is automatically created in the "
        "folder where the program is located."
    )
)

parser.add_argument(
    '--profile', '-p',
    help=(
        'Set the path to the browser profile. '
        'Example format: C:/Users/Username/AppData/Local/Google/Chrome/User Data/Default  '
        'or %%USERPROFILE%%/AppData/Local/Google/Chrome/User Data/Default '
    ),
    metavar='PATH_TO_PROFILE'
)
