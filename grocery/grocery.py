
### Breaking down the problem
# Implement a program that prompts the user for items, one per line, until the user inputs control-d
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item.
# Prefixing each line with the number of times the user inputted that item
# No need to pluralize the items. Treat the user’s input case-insensitively.


# Initialize Data Structures - Create a dictionary to store the items and their counts.
items = {}
# Collect User Inputs - Use a loop to continuously prompt the user for an item.
while True:
    item = input("Enter an item (or 'done' to finish): ").strip().lower()  # Convert input to lowercase and remove surrounding whitespace
    if item == "" or item == "done":  # Check for end-of-input signal
        break #Break out of the loop if the end-of-input signal is received.


    # Count Items
    if item in items:
        items[item] += 1  # Increment count if item exists
    else:
        items[item] = 1  # Add item with count 1 if it doesn't exist
# Prepare the Output
sorted_items = sorted(items.keys())  # Sort items alphabetically
uppercase_items = [item.upper() for item in sorted_items]  # Convert items to uppercase
# Print the Output
# Loop through the sorted items.
# For each item, print the count followed by the item name in uppercase.
for item in uppercase_items:
    print(f"{items[item]} {item}")
