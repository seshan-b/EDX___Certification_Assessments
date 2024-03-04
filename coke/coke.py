# Implement a program that prompts the user to insert a coin, one at a time,

# Info due amount to user each time.

# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.

# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.




# Function to get valid coin
def get_valid_coin():

    while True:
        coin = int(input("Insert a coin: "))

        # Check if the coin is a valid denomination the return breaks the loop
        if coin in [1, 5, 10, 25]:
            return(coin)
        else:
            print("Invalid coin. Accepted denominations are 1, 5, 10, and 25 cents.")


# The main function keeps track of the amount and checks and calculates amount giving change.
def main():
    total_amount = 0

    while total_amount < 50:
        coin = get_valid_coin()
        total_amount += coin
        print(f"Amount Due: {total_amount}")

        # Calculate and display change
        change = total_amount - 50
        if change > 0:
            print(f"Change Owed: {change}")
        else:
            print("You have reached or exceeded 50 cents. No change owed.")

if __name__ == "__main__":
    main()
