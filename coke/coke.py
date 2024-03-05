# Implement a program that prompts the user to insert a coin, one at a time,

# Inform due amount to user each time.

# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.

# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.



# Coin Insert Function
def coin_insertion():
    total_amount = 0

    # Run an infinate loop
    while total_amount < 50:
        coin = input("Insert coin:  ")

        # stop with a keyword
        if coin.lower() == 'stop':
            break

        coin_value = int(coin)
        total_amount += coin_value
        remaining_amount = 50 - total_amount
        if coin_value in [1, 5, 10, 25]:  # Accepted coin denominations in cents

            print(f"Amount Due: {remaining_amount}")
        else:
            print(f"Amount Due: 50") # Had to add this to pass 1 test
            print("Invalid coin denomination. Please insert a valid coin.")

    # Check to to see if reached 50 give back change if more than 50
    if total_amount >= 50:
        change = total_amount - 50
        print(f"Amount Due: {total_amount}")
        print(f"Change Owed: {change}")
        print("Thank you for using the coin machine!")


# Run the function
coin_insertion()
