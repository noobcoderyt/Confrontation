from colorama import Fore, Back
from pathlib import Path
import time
from functions.clear_screen import clear_screen

user_act_file = Path("user/user_act.txt")

try:
    user_act = user_act_file.read_text()

except:
    user_act_file.write_text("")
    user_act = ""

def main_menu():

    """Loads the main menu of the game."""

    print(Fore.BLUE + "\n[1] New Game")
    print(Fore.GREEN + "[2] Load Game")
    print(Fore.RED + "[3] Exit\n")

    try:
        user_input = int(input(Fore.WHITE + "> "))

    except:
        print(Fore.RED + "Please give your input in a number!\n")
        time.sleep(2)
        clear_screen()
        main_menu()

    if user_input == 1:
            pass

    elif user_input == 2:
        if user_act:
            pass
        else:
            print(Fore.RED + "\nYou don't have any saves!\n")
            time.sleep(2)
            clear_screen()
            main_menu()

    elif user_input == 3:
        quit()

main_menu()