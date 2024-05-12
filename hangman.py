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
    in_guessed = True  # Set a new bool for checking
    if not any(letter_guessed in char for char in old_letters_guessed):  # If the user guess wasn't in older guesses
        in_guessed = False  # Update if the guess wasn't already guessed before
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
    # Check valid input
    if check_valid_input(letter_guessed, old_letters_guessed) and letter_guessed not in old_letters_guessed:
        old_letters_guessed.append(letter_guessed)
        return True
    print('X')  # Input isn't valid
    sorted_old_list = sorted(old_letters_guessed)  # Print the sorted guessed letters
    for char in sorted_old_list[:-1]:
        print("{} -> ".format(char), end='')
    print(sorted_old_list[-1])
    return False


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
    discovered_word = ''  # Initialize the new string of the discovered word
    for char in secret_word:  # Iterate through the secret word
        if char in old_letters_guessed:  # If the current character was guessed by the user
            discovered_word += '{} '.format(char)  # Add the character to the correct location
        else:  # If the character wasn't guessed by the user
            discovered_word += '_ '  # Add '_' in the correct location instead
    return discovered_word  # Returns a string of the discovered word


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
    return all(char in old_letters_guessed for char in secret_word)  # Checks if all guesses are in secret word


def print_hangman(num_of_tries):
    """Prints the current stage of the game based on the number of tries the user tried guessing
        the secret word.
    param num_of_tries: the number of tries the user guessed a letter
    :type num_of_tries: int
    :return: Prints the current stage of the game based on the number of tries
    :rtype: none
    """
    print(HANGMAN_PHOTOS.get(num_of_tries))  # Prints the current stage with stage art dictionary and key


def choose_word(file_path, index):
    """Receives a file path on the system and an index, and returns a tuple
        containing the number of unique words in the word file along with the word in location index.
    :param file_path: string representing the word file path on the system
    :param index: index of word in word file
    :type file_path: string
    :type index: int
    :return: Returns a tuple containing the number of unique words in the file, and the word in location index.
    :rtype: tuple
    """
    with open(file_path, "r") as word_file:
        words = word_file.read().split()  # Splits the file content into a list of words
    unique_words = set(words)  # Creates a set of words to eliminate duplicates
    unique_count = len(unique_words)  # Counts the number of unique words
    if index < 1:  # Check if the index is less than 1
        return unique_count, None
    word_at_index = words[(index - 1) % len(words)]  # Retrieves the word at the specified index, wraps around if needed
    return unique_count, word_at_index  # Returns a tuple with the count of unique words and the word at the index


def main():
    # Defining attributes
    secret_word = ''  # Secret word string
    old_letters_guessed = []  # List of all all user guesses
    letter_guessed = ''  # Current user guess
    num_of_tries = 1  # Current count of user guesses
    first_round = True

    print_starting_message()  # Starting message of the game
    print_number_of_tries()

    #  Start of game loop
    try:
        secret_word = choose_word(r"E:\words.txt", 17)[1]  # Check for errors in word file path and set the secret word
    except Exception as e:
        print("Word file path is incorrect: {}".format(e))

    while num_of_tries < 6 and not check_win(secret_word, old_letters_guessed):  # Main game loop while no lose or win
        print("Stage: {}".format(num_of_tries), end='')
        print_hangman(num_of_tries)  # Print current hangman ASCII stage
        print("Word: ", show_hidden_word(secret_word, old_letters_guessed))  # Print the hidden word guessed letters
        letter_guessed = input("Enter your guess: ")

        # Check if the word is in the secret word and user didn't already use the word
        if try_update_letter_guessed(letter_guessed, old_letters_guessed) and (letter_guessed not in secret_word):
            num_of_tries += 1

    if num_of_tries > 5:  # Check win or lose condition and print message
        print("You lost! The word was: {}".format(secret_word))
        print_hangman(num_of_tries + 1)  # Print current hangman ASCII stage
    else:
        print("You won! The word was : {}".format(secret_word))


if __name__ == '__main__':
    main()