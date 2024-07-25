
### Breaking down the problem
# Implement a program that prompts the user for items, one per line, until the user inputs control-d
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item.
# Prefixing each line with the number of times the user inputted that item
# No need to pluralize the items. Treat the user’s input case-insensitively.


# Initialize Data Structures
items = {}

# Collect User Inputs
try:
    while True:
        item = input().strip().lower()  # Convert input to lowercase and remove surrounding whitespace
        if item == "" or item == "done":  # Check for end-of-input signal
            break

        # Count Items
        if item in items:
            items[item] += 1  # Increment count if item exists
        else:
            items[item] = 1  # Add item with count 1 if it doesn't exist
except EOFError:
    print("\nInput ended.")

# Prepare the Output
sorted_items = sorted(items.keys())  # Sort items alphabetically

# Print the Output
for item in sorted_items:  # Loop through the sorted items
    print(f"{items[item]} {item.upper()}")  # Print the count followed by the item in uppercase

