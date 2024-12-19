class colors:
    OK = "\033[92m"  # GREEN
    WARNING = "\033[93m"  # YELLOW
    FAIL = "\033[91m"  # RED
    RESET = "\033[0m"  # RESET COLOR


def green_text(text):
    return f"{colors.OK}{text}{colors.RESET}"


def red_text(text):
    return f"{colors.FAIL}{text}{colors.RESET}"


def yellow_text(text):
    return f"{colors.WARNING}{text}{colors.RESET}"
