"""Global attributes
"""
MAX_TRIES = 6

HANGMAN_ASCII_ART = r""" 
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/
"""

ERROR_1_TOO_LONG = "E1"
ERROR_2_INVALID_CHAR = "E2"
ERROR_3_ALL_ERRORS = "E3"

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
    print(HANGMAN_ASCII_ART)

def print_number_of_tries():
    """Prints the number of guesses available.
    The default amount of guesses is 6.
    :return: none
    :rtype: none
    """
    print("Tries: ", MAX_TRIES)


def is_valid_input(letter_guessed):
    """Checks whether the user input is valid. The answer must be a single letter of the english alphabet
    :param letter_guessed: exponent value
    :type letter_guessed: string
    :return: The result whether the input is valid or not.
    :rtype: bool
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha()


def main():
    print_starting_message()
    print_number_of_tries()
    print(STAGE_1)

    word = input("Please enter a word: ").lower()
    print("_ " * len(word))

    player_letter_guess = input("Guess a letter: ").lower()

    # Validation check. The input should only contain a single english letter
    print(is_valid_input(player_letter_guess))

if __name__ == '__main__':
    main()