while True:  # Loop until valid input is received
    try:
        # Prompt the user to enter the fraction in the format X/Y
        fraction = input("Enter the fraction in the format X/Y: ")  # Get user input
        X, Y = map(int, fraction.split('/'))  # Split the input and convert to integers

        # Check if Y is 0 or Y is 4
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
        elif percentage > 75:
            print("F")  # Print 'F' if the percentage is greater than 75%
        elif percentage < 50:
            print("E")  # Print 'E' if the percentage is less than 50%
        else:
            print(f"{round(percentage)}%")  # Print the actual percentage rounded to the nearest whole number

        break  # If no exception occurs and conditions are met, break out of the loop
    except ValueError:  # Catch ValueError if conversion to integer fails or invalid input format
        print("Please enter the fraction in the correct format X/Y where both X and Y are integers. Try again.")  # Inform the user of the error
    except ZeroDivisionError:  # Catch ZeroDivisionError if division by zero occurs
        print("Division by zero is not allowed. Please try again.")  # Inform the user of the error
