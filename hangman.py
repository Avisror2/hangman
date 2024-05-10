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


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks whether the user input is valid. The answer must be a single letter of the english alphabet.
    :param letter_guessed: letter guessed by the user
    :param old_letters_guessed: list of all the users guesses
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: The result whether the input is valid or not.
    :rtype: bool
    """
    in_guessed = True
    if not any(letter_guessed in char for char in old_letters_guessed):
        in_guessed = False
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and not in_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks whether the user input is valid and also not already in the list
        and updates the old_letters_guessed list to include current guess.
    :param letter_guessed: letter guessed by the user
    :param old_letters_guessed: list of all the users guesses
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: The result whether the guess was added to the list or was already in it.
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print('X')
    sorted_old_list = sorted(old_letters_guessed)
    for char in sorted_old_list[:-1]:
        print("{} -> ".format(char), end='')
    print(sorted_old_list[-1])


def main():

    print_starting_message()
    print_number_of_tries()
    print(STAGE_1)

    word = input("Please enter a word: ").lower()
    print("_ " * len(word))

    old_letters_guessed = []

    player_letter_guess = input("Guess a letter: ").lower()

    # Validation check. The input should only contain a single english letter
    try_update_letter_guessed(player_letter_guess, old_letters_guessed)


if __name__ == '__main__':
    main()