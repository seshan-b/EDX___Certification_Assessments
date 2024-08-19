# ### Breaking down the problem
# Prompts the user for names
# One per line, until the user inputs control-d.
# Assume that the user will input at least one name
# Bid adieu to those names,
# Separating two names with one and, three names with two commas and one and, and names with commas and one


# Initialize an empty list to store the names
names = []

# Loop to prompt the user for names
while True:
    try:
        # Prompt the user for a name
        name = input("Enter a name: ")
        # Append the name to the list of names
        names.append(name)
    except EOFError:
        # Break the loop if Control-D (EOF) is entered
        break

# At this point, the list 'names' contains all the user-entered names
