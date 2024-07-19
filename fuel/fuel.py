while True:
    try:
        # Prompt the user for input in the format X/Y
        input_str = input("Enter the values in X/Y format: ")

        # Split the input string into X and Y
        X_str, Y_str = input_str.split('/')

        # Convert the split parts to integers
        X = int(X_str)
        Y = int(Y_str)

        # Check if Y is zero (this will be checked for ZeroDivisionError)
        if Y == 0:
            raise ZeroDivisionError

        # Check if X is greater than Y
        if X > Y:
            raise ValueError("X is greater than Y")

        # If all validations pass, break the loop
        break

    except ValueError as ve:
        # Catch ValueError and prompt the user again
        print(f"Invalid input: {ve}. Please enter integers where X <= Y and Y != 0.")

    except ZeroDivisionError:
        # Catch ZeroDivisionError and prompt the user again
        print("Y cannot be zero. Please enter integers where X <= Y and Y != 0.")

# Calculate the percentage
percentage = (X / Y) * 100

# Determine the output based on the percentage
if percentage >= 99:
    output = "F"
elif percentage <= 1:
    output = "E"
else:
    output = f"{int(round(percentage))}%"

# Print the output
print(output)
