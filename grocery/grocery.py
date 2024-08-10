# ### Breaking down the problem
# # Implement a program that prompts the user for items, one per line, until the user inputs control-d
# # Then output the user’s grocery list in all uppercase, sorted alphabetically by item.
# # Prefixing each line with the number of times the user inputted that item
# # No need to pluralize the items. Treat the user’s input case-insensitively.

# # Initialize Data Structures
# # Create an empty dictionary to store the items and their counts
# items = {}

# # Collect User Inputs
# try:
#     # Use a loop to continuously ask the user for input
#     while True:
#         # Prompt the user to enter an item, convert it to lowercase, and remove any extra spaces around it
#         item = input().strip().lower()
#         # Check if the input is empty or the user typed 'done' to finish input
#         if item == "" or item == "done":
#             # If so, break out of the loop
#             break

#         # Count Items
#         # Check if the item is already in the dictionary
#         if item in items:
#             # If it is, increment its count by 1
#             items[item] += 1
#         else:
#             # If it's not, add the item to the dictionary with a count of 1
#             items[item] = 1
# # Handle the EOFError exception, which occurs if the user inputs control-d
# except EOFError:
#     # Do nothing and just pass the exception
#     pass

# # Prepare the Output
# # Get a list of the dictionary's keys (items) and sort them alphabetically
# sorted_items = sorted(items.keys())

# # Print the Output
# # Loop through the sorted list of items
# for item in sorted_items:
#     # Print the count of the item followed by the item name in uppercase
#     print(f"{items[item]} {item.upper()}")



### Redone version.
from collections import defaultdict

def get_grocery_list():
    # Using defaultdict to simplify counting
    items = defaultdict(int)

    try:
        while True:
            item = input().strip().lower()
            if not item:  # Empty string ends input
                break
            items[item] += 1  # Increment item count
    except EOFError:
        pass  # Handle EOF (Control-D) gracefully

    # Sort items alphabetically and output them
    for item in sorted(items):
        print(f"{items[item]} {item.upper()}")

# Call the function to execute the program
get_grocery_list()
