# ### Breaking down the problem
# Prompts the user for a level, If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.


# Start a loop that will continue until the user inputs a valid positive integer for the level
while True:
    # Prompt the user for input
    user_input = input("Enter a level: ")

    # Try to convert the input to an integer
    try:
        level = int(user_input)

        # Check if the integer is a positive number
        if level > 0:
            break  # Exit the loop if the level is valid
        else:
            print("Please enter a positive integer.")

    # If the input could not be converted to an integer, handle the error
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Once we have a valid level, generate a random number between 1 and the level (inclusive)
import random
number_to_guess = random.randint(1, level)

# Start another loop to prompt the user to guess the number
while True:
    # Prompt the user to guess the number
    user_input = input("Guess the number: ")

    # Try to convert the input to an integer
    try:
        guess = int(user_input)

        # Check if the guess is a positive number
        if guess > 0:
            # Compare the guess to the generated number
            if guess < number_to_guess:
                print("Too small!")
            elif guess > number_to_guess:
                print("Too large!")
            else:
                print("Just right!")
                break  # Exit the loop when the correct number is guessed
        else:
            print("Please enter a positive integer.")

    # If the input could not be converted to an integer, handle the error
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
