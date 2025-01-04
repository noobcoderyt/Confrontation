import time

def display_text(string, delay=0.1):

    """Display any string given with a typewriter animation."""

    for character in string:
        print(character, end="", flush=True)
        time.sleep(delay)


def display_ascii(ascii, delay=0.1):
    
    """Display any ASCII art with a transition effect."""

    for line in ascii:
        print(line)
        time.sleep(delay)
