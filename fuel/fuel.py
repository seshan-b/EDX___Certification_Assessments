# This loop will keep running until we get valid input
while True:
    try:
        # Ask the user to input values in the format X/Y
        input_str = input("Enter the values in X/Y format: ")

        # Split the input string into X and Y parts
        X_str, Y_str = input_str.split('/')

        # Convert the parts into integers
        X = int(X_str)
        Y = int(Y_str)

        # Check if Y is zero, which would cause an error when dividing
        if Y == 0:
            raise ZeroDivisionError

        # Check if X is greater than Y, which is not allowed
        if X > Y:
            raise ValueError("X is greater than Y")

        # If we reach here, the input is valid, so we break out of the loop
        break

    except ValueError as ve:
        # If there is a ValueError (invalid input), print an error message
        print(f"Invalid input: {ve}. Please enter integers where X <= Y and Y != 0.")

    except ZeroDivisionError:
        # If there is a ZeroDivisionError (Y is zero), print an error message
        print("Y cannot be zero. Please enter integers where X <= Y and Y != 0.")

# Calculate the percentage of X divided by Y
percentage = (X / Y) * 100

# Decide what to output based on the percentage
if percentage >= 99:
    output = "F"  # 99% or more is an "F"
elif percentage <= 1:
    output = "E"  # 1% or less is an "E"
else:
    output = f"{int(round(percentage))}%"  # Otherwise, output the rounded percentage

# Print the final result
print(output)
