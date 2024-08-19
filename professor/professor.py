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
    """
    Main function to run the math quiz.
    Prompts the user for a level, generates 10 math problems, and calculates the score.
    """
    # Step 1: Get the level from the user
    level = get_level()

    # Step 2: Initialize the score counter
    score = 0

    # Step 3: Generate and solve 10 problems
    for _ in range(10):
        # Generate two random integers based on the level
        x = generate_integer(level)
        y = generate_integer(level)

        # Calculate the correct answer
        correct_answer = x + y

        # Attempt counter
        attempts = 0

        while attempts < 3:
            try:
                # Prompt the user for an answer
                user_answer = int(input(f"{x} + {y} = "))

                # Check if the user's answer is correct
                if user_answer == correct_answer:
                    score += 1  # Increment score if correct
                    break  # Exit the loop if the answer is correct
                else:
                    print("EEE")  # Incorrect answer, print "EEE"
            except ValueError:
                print("EEE")  # If input is not an integer, print "EEE"

            attempts += 1  # Increment the attempt counter

        # If the user failed to answer correctly after 3 attempts
        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")

    # Step 4: Display the final score
    print(f"Score: {score}")


def get_level():
    """
    Prompt the user for a level (1, 2, or 3).
    If the input is valid, return the level as an integer.
    If the input is invalid, keep prompting the user until a valid input is provided.
    """
    while True:  # Loop until valid input is provided
        try:
            # Prompt the user for input
            level = int(input("Enter a level (1, 2, or 3): "))
            # Check if the input is one of the valid levels
            if level in [1, 2, 3]:
                return level  # Valid input, return the level
        except ValueError:
            pass  # If input is not an integer, continue looping

        # If input is invalid, print an error message and loop again
        print("Invalid input. Please enter 1, 2, or 3.")



def generate_integer(level):
    """
    Generate a random integer based on the difficulty level.
    Level 1: 1-digit integer (0-9)
    Level 2: 2-digit integer (10-99)
    Level 3: 3-digit integer (100-999)
    """
    if level == 1:
        return random.randint(0, 9)  # Generate a 1-digit integer
    elif level == 2:
        return random.randint(10, 99)  # Generate a 2-digit integer
    elif level == 3:
        return random.randint(100, 999)  # Generate a 3-digit integer



if __name__ == "__main__":
    main()
