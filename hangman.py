"""Global attributes
"""
amount_of_tries = 6

STAGE_1 = """
x-------x
"""
STAGE_2 = """    
    x-------x
    |
    |
    |
    |
    |
"""
STAGE_3 = """
    x-------x
    |       |
    |       0
    |
    |
    |
"""
STAGE_4 = """
    x-------x
    |       |
    |       0
    |       |
    |
    |
"""
STAGE_5 = r"""
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
"""
STAGE_6 = r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
"""
STAGE_7 = r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
"""

def print_starting_message():
    """Prints the starting message of the game.
    :return: none
    :rtype: none
    """
    print("Welcome to the game Hangman")
    print(r""" 
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/""")

def print_number_of_tries():
    """Prints the number of guesses available.
    The default amount of guesses is 6.
    :return: none
    :rtype: none
    """
    print("Tries: ", amount_of_tries)


def main():
    print_starting_message()
    print_number_of_tries()
    print(STAGE_1)


if __name__ == '__main__':
    main()