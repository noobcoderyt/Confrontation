import time
from colorama import Fore, Back

RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
WHITE = Fore.WHITE
BLACK_BG = Back.BLACK

def display_text(string, color=WHITE, bg=BLACK_BG, delay=0.1):

    """Displays any string given with a typewriter animation."""

    for character in string:
        print(color + character, end="", flush=True)
        time.sleep(delay)


def display_ascii(ascii, color=WHITE, bg=BLACK_BG, delay=0.1):
    
    """Displays any ASCII art with a transition effect."""

    for line in ascii:
        print(color + line)
        time.sleep(delay)
