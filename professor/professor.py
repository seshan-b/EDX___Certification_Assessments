# ### Breaking down the problem
# Prompts the user for a level, If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits.
# No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
# The program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
# If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.


import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
