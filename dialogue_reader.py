from pathlib import Path
from colorama import Fore
from functions.display_text import display_text

RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW

def dialogue_reader(file_name, color=WHITE):

    """Prints the dialogue in a given file."""

    dialogue_path = Path(f"dialogues/{file_name}")
    dialogue = dialogue_path.read_text()

    display_text(f"{dialogue}", color, delay=0.05)
