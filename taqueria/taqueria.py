#  Implement a program that enables a user to place an order
# prompting them for items, one per line, until the user inputs control-d
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($)
# Treat the user’s input case insensitively. Ignore any input that isn’t an item.
# Assume that every item on the menu will be title-cased.


menu = {
    "Burger": 5.99,
    "Fries": 2.99,
    "Soda": 1.49,
    "Salad": 3.99
}

# Print the menu to verify
print("Menu:")
for item, price in menu.items():
    print(f"{item}: ${price}")


