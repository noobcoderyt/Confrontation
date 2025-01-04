from pathlib import Path
import time
from functions.clear_screen import clear_screen
from functions.display_text import display_ascii, display_text, GREEN

def intro():

    """Loads the intro of the game."""

    logo_path = Path("ascii/logo.txt")
    logo = logo_path.read_text().splitlines()
    display_ascii(logo)

    time.sleep(4)
    clear_screen()
    
    developers_path = Path("ascii/developers.txt")
    developers = developers_path.read_text().splitlines()
    display_ascii(developers)

    time.sleep(4)
    clear_screen()

    display_text("Please Play The Game In Fullscreen For The Best Experience.".center(20), color=GREEN)
