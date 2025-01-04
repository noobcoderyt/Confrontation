import platform
import os

operating_system = platform.system()

def clear_screen():

    """Checks if the user is on Windows, Linux or Mac."""

    if operating_system.lower() == "windows":
        os.system("cls")
    elif operating_system.lower() == "linux":
        os.system("clear")
    elif operating_system.lower() == "darwin":
        os.system("clear")
