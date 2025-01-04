from colorama import Fore, Back
from pathlib import Path
import time
from functions.clear_screen import clear_screen
from act1 import act1

user_act_file = Path("user/user_act.txt")

try:
    user_act = int(user_act_file.read_text())

except:
    user_act_file.write_text("")
    user_act = ""

def main_menu():

    """Loads the main menu of the game."""

    print(Fore.BLUE + "\n\t[1] New Game")
    print(Fore.GREEN + "\t[2] Load Game")
    print(Fore.RED + "\t[3] Exit\n")

    try:
        user_input = int(input(Fore.WHITE + "\t> "))

    except:
        print(Fore.RED + "\tPlease give your input in a number!\n")
        time.sleep(2)
        clear_screen()
        main_menu()

    if user_input == 1:
            act1()

    elif user_input == 2:

        if user_act:
            pass
        else:
            print(Fore.RED + "\n\tYou don't have any saves!\n")
            time.sleep(2)
            clear_screen()
            main_menu()

    elif user_input == 3:
        quit()
