from pathlib import Path
from functions.display_text import display_ascii, RED
from tqdm import tqdm
import time
from colorama import Fore
from functions.clear_screen import clear_screen
from dialogue_reader import dialogue_reader, YELLOW
from functions.display_text import brute_force_effect

user_act_file = Path("user/user_act.txt")

act1_path = Path("ascii/act1.txt")
act1_logo = act1_path.read_text().splitlines()

def act1():

    """Loads the Act 1 of the game."""

    user_act_file.write_text("1")

    print(Fore.CYAN + "\n")

    for i in tqdm(range(100), desc="Loading Act 1"):
        time.sleep(0.05)

    time.sleep(0.5)
    clear_screen()
    display_ascii(act1_logo, RED)
    time.sleep(2)
    clear_screen()

    dialogue_reader("narrator1.txt", "Narrator", YELLOW)
    time.sleep(4)
    clear_screen()
    brute_force_effect("However")
    time.sleep(2)
    clear_screen()

    dialogue_2_path = Path("dialogues/narrator2.txt")
    dialogue_2 = dialogue_2_path.read_text()

    brute_force_effect(dialogue_2)
    time.sleep(4)
