from pathlib import Path
import time
from functions.clear_screen import clear_screen
from functions.display_text import display_ascii, display_text, GREEN
from tqdm import tqdm

def intro():

    """Loads the intro of the game."""

    logo_path = Path("ascii/logo.txt")
    logo = logo_path.read_text().splitlines()
    display_ascii(logo)

    for i in tqdm(range(100), desc="Loading Game"):
        time.sleep(0.01)

    time.sleep(2)
    clear_screen()
    
    developers_path = Path("ascii/developers.txt")
    developers = developers_path.read_text().splitlines()
    display_ascii(developers)

    time.sleep(4)
    clear_screen()

    display_text("\n\tPlease Play The Game In Fullscreen For The Best Experience.\n", color=GREEN)
    time.sleep(2)
    clear_screen()
