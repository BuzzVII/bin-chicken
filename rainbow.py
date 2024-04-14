RESET = "\033[0m"
BOLD = "\033[01m"
DISABLE = "\033[02m"
UNDERLINE = "\033[04m"
REVERSE = "\033[07m"
STRIKETHROUGH = "\033[09m"
INVISIBLE = "\033[08m"


class Text:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    ORANGE = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    LIGHTGREY = "\033[37m"
    DARKGREY = "\033[90m"
    LIGHTRED = "\033[91m"
    LIGHTGREEN = "\033[92m"
    YELLOW = "\033[93m"
    LIGHTBLUE = "\033[94m"
    PINK = "\033[95m"
    LIGHTCYAN = "\033[96m"


class Background:
    BLACK = "\033[40m"
    RED = "\033[41m"
    GREEN = "\033[42m"
    ORANGE = "\033[43m"
    BLUE = "\033[44m"
    PURPLE = "\033[45m"
    CYAN = "\033[46m"
    LIGHTGREY = "\033[47m"


def black(msg: str) -> str:
    return Text.BLACK + msg + RESET


def red(msg: str) -> str:
    return Text.RED + msg + RESET


def green(msg: str) -> str:
    return Text.GREEN + msg + RESET


def orange(msg: str) -> str:
    return Text.ORANGE + msg + RESET


def blue(msg: str) -> str:
    return Text.BLUE + msg + RESET


def yellow(msg: str) -> str:
    return Text.YELLOW + msg + RESET


def purple(msg: str) -> str:
    return Text.PURPLE + msg + RESET


def cyan(msg: str) -> str:
    return Text.CYAN + msg + RESET


def lightgrey(msg: str) -> str:
    return Text.LIGHTGREY + msg + RESET


def print_error(msg: str) -> None:
    print(BOLD, end="")
    print(UNDERLINE, end="")
    print(red(msg), end="")
    print(RESET)


def print_warning(msg: str) -> None:
    print(BOLD, end="")
    print(yellow(msg), end="")
    print(RESET)


if __name__ == "__main__":
    print_error("ERROR TEST")
    print_warning("WARNING TEST")
