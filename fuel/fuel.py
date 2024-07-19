while True:  # Loop until valid input is received
    try:
        # Prompt the user for input values of X and Y
        X = int(input("Enter value for X: "))  # Convert input to integer
        Y = int(input("Enter value for Y: "))  # Convert input to integer

        # Check if X is greater than Y or Y is 0
        if X > Y:
            print("X should not be greater than Y. Please try again.")  # Inform the user of the error
            continue  # Continue to the next iteration of the loop to prompt the user again
        if Y == 0:
            print("Y should not be 0. Please try again.")  # Inform the user of the error
            continue  # Continue to the next iteration of the loop to prompt the user again

        break  # If no exception occurs and conditions are met, break out of the loop
    except ValueError:  # Catch ValueError if conversion to integer fails
        print("Both X and Y need to be integers. Please try again.")  # Inform the user of the error
