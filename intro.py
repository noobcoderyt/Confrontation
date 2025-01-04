from pathlib import Path
import time
from functions.clear_screen import clear_screen
from functions.display_text import display_ascii, display_text

def intro():

    """Load the intro of the game."""

    logo_path = Path("ascii/logo.txt")
    logo = logo_path.read_text().splitlines()
    display_ascii(logo)

    time.sleep(3)
    clear_screen()
    
    developers_path = Path("ascii/developers.txt")
    developers = developers_path.read_text().splitlines()
    display_ascii(developers)

    time.sleep(3)
    clear_screen()

    display_text("Please Play The Game In Fullscreen For Best Experience.".center(20))

intro()
