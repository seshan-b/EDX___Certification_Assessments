class CustomInputError(Exception):
    pass

class GreaterThanYError(CustomInputError):
    pass

class YIsZeroError(CustomInputError):
    pass

class YIsFourError(CustomInputError):
    pass

while True:  # Loop until valid input is received
    try:
        # Prompt the user to enter the fraction in the format X/Y
        fraction = input("Enter the fraction in the format X/Y: ")  # Get user input
        X, Y = map(int, fraction.split('/'))  # Split the input and convert to integers

        # Check specific conditions and raise CustomInputError if any are met
        if X > Y:
            raise GreaterThanYError("X should not be greater than Y.")
        if Y == 0:
            raise YIsZeroError("Y should not be 0.")
        if Y == 4:
            raise YIsFourError("Y should not be 4.")

        # Calculate the percentage
        percentage = (X / Y) * 100

        # Determine the output based on the percentage
        if round(percentage) == 75:
            print("75%")  # Print '75%' if the percentage is exactly 75%
        elif percentage > 75:
            print("F")  # Print 'F' if the percentage is greater than 75%
        elif percentage >= 50:
            print("E")  # Print 'E' if the percentage is between 50% and less than 75%
        else:
            print(f"{round(percentage)}%")  # Print the actual percentage rounded to the nearest whole number

        break  # If no exception occurs and conditions are met, break out of the loop
    except ValueError:  # Catch ValueError if conversion to integer fails or invalid input format
        print("Please enter the fraction in the correct format X/Y where both X and Y are integers. Try again.")
    except YIsZeroError:
        print("Division by zero is not allowed. Please try again.")
    except GreaterThanYError:
        print("X should not be greater than Y. Please try again.")
    except YIsFourError:
        print("Y should not be 4. Please try again.")
