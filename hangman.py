"""Global attributes
"""
# Maximum number of tries before game loss
MAX_TRIES = 6

# ASCII art for game header
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

# The ASCII art for the different stages of the game
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
    |      / \
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

# Dictionary of all the stages ASCII art combined
HANGMAN_PHOTOS = {1: STAGE_1, 2: STAGE_2, 3: STAGE_3, 4: STAGE_4, 5: STAGE_5, 6: STAGE_6, 7: STAGE_7}


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


def show_hidden_word(secret_word, old_letters_guessed):
    """Receives the secret word and current user character guesses via list, and returns an appropriate message
        containing the current correct user guesses from the secret_word.
    :param secret_word: the secret word of the game
    :param old_letters_guessed: list of all the users guesses
    :type secret_word: string
    :type old_letters_guessed: list
    :return: Returns a string containing the current correct guesses of characters of the secret word.
    :rtype: string
    """
    discovered_word = ''
    for char in secret_word:
        if char in old_letters_guessed:
            discovered_word += '{} '.format(char)
        else:
            discovered_word += '_ '
    return discovered_word


def check_win(secret_word, old_letters_guessed):
    """Receives the secret word and current user character guesses via list,
        and returns True if the user guessed the word.
    :param secret_word: the secret word of the game
    :param old_letters_guessed: list of all the users guesses
    :type secret_word: string
    :type old_letters_guessed: list
    :return: Returns True if the user guessed the word correctly.
    :rtype: bool
    """
    return all(char in old_letters_guessed for char in secret_word)


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS.get(num_of_tries))


def main():
    print('')


if __name__ == '__main__':
    main()