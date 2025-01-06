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

access_granted_path = Path("ascii/access_granted.txt")
access_granted = access_granted_path.read_text().splitlines()

access_denied_path = Path("ascii/access_denied.txt")
access_denied = access_denied_path.read_text().splitlines()

linus_ascii_path = Path("ascii/linus.txt")
linus_ascii = linus_ascii_path.read_text().splitlines()

dialogue_2_path = Path("dialogues/narrator2.txt")
dialogue_2 = dialogue_2_path.read_text()

linus_files = ["OpenAI_Secrets", "Gemini_Jailbreaks", "temp", "devin_key.txt"]
open_ai_files = ["ChatGPT-4o-Model", "speech.txt", "pass.txt", "tester.c", "competitors.xlsx"]
system_wipeout_commands = [
    "sudo rm -rf / --no-preserve-root",
    "sudo rm -rf /* --no-preserve-root",
    "sudo rm -rf /",
    "sudo rm -rf /*",
    "sudo find / -type f -exec rm -f {} +",
    "sudo find / -type f -delete",
    "sudo find / -type f -exec shred -u {} +",
    "sudo dd if=/dev/zero of=/dev/sda bs=1M",
    "sudo dd if=/dev/urandom of=/dev/sda bs=1M",
    "sudo mkfs.ext4 /dev/sda",
    "sudo mkfs.xfs /dev/sda",
    "sudo rsync -a --delete /dev/null /",
    "sudo bash -c 'for i in /*; do rm -rf \"$i\"; done'",
    "sudo rm -rf /home/*",
    "sudo rm -rf /var/*"
]
password_attempts = 3

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

    display_ascii(linus_ascii)

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
            print(Fore.RED + "The directory is not empty. Did you mean 'rm -r temp' ?")
        else:
            print(Fore.RED + "You cannot use that command for this mission.")
        
    clear_screen()

    dialogue_reader("unknown_person2.txt", BLUE)
    dialogue_reader("linus2.txt")
    dialogue_reader("arthur1.txt", BLUE)
    dialogue_reader("linus3.txt")
    dialogue_reader("arthur2.txt", BLUE)

    time.sleep(2)

    brute_force_effect("Mission 2: Wipeout: Wipe all files from the PC.")

    time.sleep(2)
    clear_screen()

    display_ascii(linus_ascii)

    mission_completed = False
    while mission_completed != True:
        print(Fore.RED + "openai@debian:", end="")
        print(Fore.BLUE + "~/Desktop", end="")
        print(Fore.WHITE + "$ ", end="")
        user_input = input(Fore.WHITE + "")

        if user_input == "ls":
            for file in open_ai_files:
                print(file)
        elif user_input in system_wipeout_commands:
            print(Fore.WHITE + "[sudo] password for openai: ", end="")
            user_input = input(Fore.WHITE + "")
            if user_input == "openai_server_9124":
                display_ascii(access_granted, color=GREEN)
                for i in tqdm(range(100), desc=Fore.RED + "Access granted. Wiping out system..."):
                    time.sleep(random.uniform(0.1, 0.01))
                brute_force_effect("Mission Completed!", color=BLUE)
                time.sleep(3)
                clear_screen()
            else:
                if password_attempts == 0:
                    print(Fore.RED + "Attempt 3 Failed. System has been locked for 24 hours.")
                    brute_force_effect("Mission Failed.", color=RED)
                    act1()
                else:
                    display_ascii(access_denied, color=RED)
                    print(Fore.RED + "Error: Wrong Password. You have two attempts left.")
                    password_attempts -= 1
        elif user_input == "cat pass.txt":
            print(Fore.WHITE + "openai_server_9124")
        else:
            print(Fore.RED + "You cannot use that command on this mission.")
