import time
from colorama import Fore, Back
import random

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


def brute_force_effect(string, color=WHITE):

    """Displays any given string with brute force animation."""

    characters = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>?,./:;"[]}{|`~'
    for target_char in string:
        for char in characters:
            print(color + char, end='', flush=True)
            time.sleep(random.uniform(0.01, 0.001))
            if char == target_char:
                break
            print("\b", end='', flush=True)
