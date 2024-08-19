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

# Initialize the farewell message with "Adieu, adieu, to "
farewell_message = "Adieu, adieu, to "

# Handle the different cases based on the number of names

if len(names) == 1:
    # If there is only one name, append it directly to the farewell message
    farewell_message += names[0]

elif len(names) == 2:
    # If there are two names, join them with " and "
    farewell_message += names[0] + " and " + names[1]

else:
    # If there are three or more names
    # Join all names except the last one with ", "
    farewell_message += ", ".join(names[:-1])
    # Add " and " followed by the last name
    farewell_message += ", and " + names[-1]

# Print the final farewell message
print(farewell_message)
