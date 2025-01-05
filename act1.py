from pathlib import Path
from functions.display_text import display_ascii, RED
from tqdm import tqdm
import time
from colorama import Fore
from functions.clear_screen import clear_screen
from dialogue_reader import dialogue_reader, YELLOW, BLUE, GREEN, CYAN
from functions.display_text import brute_force_effect
import random

user_act_file = Path("user/user_act.txt")

act1_path = Path("ascii/act1.txt")
act1_logo = act1_path.read_text().splitlines()

dialogue_2_path = Path("dialogues/narrator2.txt")
dialogue_2 = dialogue_2_path.read_text()

linus_files = ["OpenAI_Secrets", "Gemini_Jailbreaks", "temp", "devin_key.txt"]

def act1():

    """Loads the Act 1 of the game."""

    user_act_file.write_text("1")

    print(Fore.CYAN + "\n")

    for i in tqdm(range(100), desc="Loading Act 1"):
        time.sleep(random.uniform(0.01, 0.05))

    time.sleep(0.5)
    clear_screen()
    display_ascii(act1_logo, RED)
    brute_force_effect("Your Game Will Be Saved Everytime You Complete An Act.")
    time.sleep(2)
    clear_screen()

    dialogue_reader("narrator1.txt", YELLOW)
    time.sleep(4)
    clear_screen()
    brute_force_effect("However", YELLOW)
    time.sleep(2)
    clear_screen()

    brute_force_effect(dialogue_2, YELLOW)

    time.sleep(4)
    clear_screen()

    dialogue_reader("unknown_person1.txt", color=BLUE, delay=0.1)
    time.sleep(1)
    dialogue_reader("linus1.txt", delay=0.1)
    time.sleep(2)
    clear_screen()

    dialogue_reader("mission1.txt", color=CYAN)
    time.sleep(4)
    clear_screen()

    mission_completed = False
    while mission_completed != True:
        print(Fore.GREEN + "linus@linuxmint:~$ ", end="")
        user_input = input(Fore.WHITE + "")
        if user_input == "ls":
            for file in linus_files:
                print(file)
        elif user_input == "rm -r temp" or user_input == "rm -r 'temp'" or user_input == "rm -r temp/":
            print("'temp' directory has been deleted.\n")
            brute_force_effect("Mission Completed!", color=BLUE)
            time.sleep(3)
            mission_completed = True
        elif "rmdir" in user_input:
            print(Fore.RED + "Error: The directory is not empty. Did you mean 'rm -r temp' ?")
        else:
            print(Fore.RED + "Error: You cannot use that command for this mission.")
