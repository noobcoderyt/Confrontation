from pathlib import Path
import time
from functions.clear_screen import clear_screen
from functions.display_text import display_ascii, display_text, GREEN
from tqdm import tqdm
import random

logo_path = Path("ascii/logo.txt")
logo = logo_path.read_text().splitlines()
developers_path = Path("ascii/developers.txt")
developers = developers_path.read_text().splitlines()

def intro():

    """Loads the intro of the game."""

    display_ascii(logo)

    for i in tqdm(range(100), desc="Loading Game"):
        time.sleep(random.uniform(0.01, 0.1))

    time.sleep(2)
    clear_screen()
    
    display_ascii(developers)

    time.sleep(4)
    clear_screen()

    display_text("\n\tPlease Play The Game In Fullscreen For The Best Experience.\n", color=GREEN)
    time.sleep(2)
    clear_screen()
