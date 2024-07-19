while True:  # Loop until valid input is received
    try:
        # Prompt the user for input values of X and Y
        X = int(input("Enter value for X: "))  # Convert input to integer
        Y = int(input("Enter value for Y: "))  # Convert input to integer

        # Check if X is greater than Y, Y is 0, or Y is 4
        if X > Y:
            print("X should not be greater than Y. Please try again.")  # Inform the user of the error
            continue  # Continue to the next iteration of the loop to prompt the user again
        if Y == 0:
            print("Y should not be 0. Please try again.")  # Inform the user of the error
            continue  # Continue to the next iteration of the loop to prompt the user again
        if Y == 4:
            print("Y should not be 4. Please try again.")  # Inform the user of the error
            continue  # Continue to the next iteration of the loop to prompt the user again

        # Perform a division to demonstrate catching ZeroDivisionError
        result = X / Y  # This is where ZeroDivisionError might occur
        print(f"The result of {X} divided by {Y} is {result}")  # Print the result if no exception occurs
        break  # If no exception occurs and conditions are met, break out of the loop
    except ValueError:  # Catch ValueError if conversion to integer fails
        print("Both X and Y need to be integers. Please try again.")  # Inform the user of the error
    except ZeroDivisionError:  # Catch ZeroDivisionError if division by zero occurs
        print("Division by zero is not allowed. Please try again.")  # Inform the user of the error
