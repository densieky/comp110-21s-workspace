"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730322721"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Finding your fortune."""
    your_message: int = randint(0, 100)
    if your_message > 75:
        return "Here comes the sun."
    else: 
        if your_message < 25:
            return "Something brand new is headed your way."
        else:
            if your_message > 50:
                return "People are waiting for you to be exactly who you are."
            else:
                return "It's alright."


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
