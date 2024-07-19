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

        # Calculate the percentage
        percentage = (X / Y) * 100

        # Determine the output based on the percentage
        if percentage == 75:
            print("75%")  # Print '75%' if the percentage is exactly 75%
        elif 50 <= percentage < 75:
            print("E")  # Print 'E' if the percentage is between 50% and less than 75%
        elif percentage >= 75:
            print("F")  # Print 'F' if the percentage is 75% or above
        else:
            print(f"{round(percentage)}%")  # Print the actual percentage rounded to the nearest whole number

        break  # If no exception occurs and conditions are met, break out of the loop
    except ValueError:  # Catch ValueError if conversion to integer fails
        print("Both X and Y need to be integers. Please try again.")  # Inform the user of the error
    except ZeroDivisionError:  # Catch ZeroDivisionError if division by zero occurs
        print("Division by zero is not allowed. Please try again.")  # Inform the user of the error
