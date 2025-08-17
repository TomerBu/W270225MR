from random import choice, randint
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def random_lower():
    return choice(ascii_lowercase)

def random_upper():
    return choice(ascii_uppercase)

def random_digit(): 
    return choice(digits)

def random_punctuation():
    return choice(punctuation)


def get_int(message = "Enter a number: "):

    while True:
        user_input = input(message)

        if user_input.isdigit():
            return int(user_input)
        print("try again")

def get_boolean(message = "boolean True/False Yes/No: "):

    while True:
        user_input = input(message)

        if user_input.lower() in ["yes", "yap", "yeah", "y", "true", "yy", "yep", "sure", "1"]:
            return True
        elif user_input.lower() in ["no", "nah", "n", "false", "nope", "0"]:
            return False
        print("try again")


def get_letter(message="Enter a single letter: "):
    while True:
        user_input = input(message).strip()
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
       
        print("try again.")
 

def underscores(num:int):
    """
    Returns a list of underscores of length num.
    If num is 5, it returns ["_", "_", "_", "_", "_"].
    If num is 0, it returns an empty list.
    If num is negative, it returns an empty list.
    """
    # return "_" * num
    return ["_"] * num


def avg(*numbers):
    return sum(numbers) / len(numbers)

def stats(*numbers):
    """
        Returns the minimum, maximum, and total of the given numbers.
        Example: stats(1, 2, 3, 4, 5) returns (1, 5, 15)
        min, max, total = stats(1, 2, 3, 4, 5)

        print(stats(1, 2, 3, 4, 5)) # (1, 5, 15)
        print(stats(1, 2, 3, 4, 5)[0]) # 1
    """
    return min(numbers), max(numbers),  sum(numbers)

result = stats(1, 2, 3, 4, 5)

print(result) # (1, 5, 15)

