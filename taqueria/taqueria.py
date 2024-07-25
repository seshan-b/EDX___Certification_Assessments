
### Breaking down the problem
# Implement a program that enables a user to place an order
# prompting them for items, one per line, until the user inputs control-d
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($)
# Treat the user’s input case insensitively. Ignore any input that isn’t an item.
# Assume that every item on the menu will be title-cased.


# Define the menu with items and their respective prices
menu = {
    "Burger": 5.99,
    "Fries": 2.99,
    "Soda": 1.49,
    "Salad": 3.99
}

# Initialize the total cost to zero
total_cost = 0

# Inform the user how to enter items and how to finish input
print("Enter items one per line (Press Ctrl-D to finish):")

try:
    # Start an infinite loop to continuously prompt the user for input
    while True:
        # Prompt the user for input, remove leading/trailing whitespace, and convert to title case
        item = input().strip().title()

        # Check if the entered item exists in the menu
        if item in menu:
            # Add the price of the item to the total cost
            total_cost += menu[item]
            # Display the current total cost formatted to 2 decimal places
            print(f"${total_cost:.2f}")
        else:
            # If the item does not exist in the menu, ignore the input and continue
            pass
except EOFError:
    # Handle the end-of-file (Ctrl-D) to end the input loop
    print("\nOrder complete.")
    # Display the final total cost formatted to 2 decimal places
    print(f"Total cost: ${total_cost:.2f}")

