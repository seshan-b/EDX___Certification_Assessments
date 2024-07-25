
### Breaking down the problem
# Implement a program that enables a user to place an order
# prompting them for items, one per line, until the user inputs control-d
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($)
# Treat the user’s input case insensitively. Ignore any input that isn’t an item.
# Assume that every item on the menu will be title-cased.


# This dictionary stores the menu items and their prices
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# This variable will keep track of the total cost of all the items ordered
total_cost = 0

# Print a message to tell the user how to enter items and how to finish input
print("Enter items one per line (Press Ctrl-D to finish):")

try:
    # This loop will keep asking the user for input until they press Ctrl-D
    while True:
        # Get the user's input, remove any extra spaces, and capitalize the first letter of each word
        item = input().strip().title()

        # Check if the item is in the menu
        if item in menu:
            # If the item is in the menu, add its price to the total cost
            total_cost += menu[item]
            # Print the current total cost with a dollar sign and two decimal places
            print(f"${total_cost:.2f}")
        else:
            # If the item is not in the menu, do nothing and continue asking for input
            pass
except EOFError:
    # When the user presses Ctrl-D, print a message saying the order is complete
    print("\nOrder complete.")
    # Print the final total cost with a dollar sign and two decimal places
    print(f"Total cost: ${total_cost:.2f}")
