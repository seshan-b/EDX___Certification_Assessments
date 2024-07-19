while True:  # Loop until valid input is received
    try:
        # Prompt the user for input values of X and Y
        X = int(input("Enter value for X: "))  # Convert input to integer
        Y = int(input("Enter value for Y: "))  # Convert input to integer
        break  # If no exception occurs, break out of the loop
    except ValueError:  # Catch ValueError if conversion to integer fails
        print("Both X and Y need to be integers. Please try again.")  # Inform the user of the error
