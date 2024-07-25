
### Breaking down the problem
# Implement a program that prompts the user for items, one per line, until the user inputs control-d
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item.
# Prefixing each line with the number of times the user inputted that item
# No need to pluralize the items. Treat the user’s input case-insensitively.


# Initialize Data Structures - Create a dictionary to store the items and their counts.
# Collect User Inputs - Use a loop to continuously prompt the user for an item.
# Convert each input to a consistent case (e.g., all lowercase).
# Check for an end-of-input signal (simulate control-d with an empty input or a specific keyword like "done").
# Break out of the loop if the end-of-input signal is received.
# Step 3: Count Items
# For each input item, check if it already exists in the dictionary:
# If it does, increment the count for that item.
# If it doesn't, add the item to the dictionary with a count of 1.
# Step 4: Prepare the Output
# Extract the items from the dictionary.
# Convert each item to uppercase.
# Sort the items alphabetically.
# Step 5: Print the Output
# Loop through the sorted items.
# For each item, print the count followed by the item name in uppercase.
