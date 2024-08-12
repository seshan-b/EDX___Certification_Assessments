# ### Breaking down the problem
# Prompt User for string
# Output the "emojized" version of that string
# Convert any codes (or aliases) therein to their corresponding emoji.


import emoji

# Prompt the user for a string
user_input = input("Please enter a string: ")

# Convert the aliases in the string to their corresponding emojis
emojized_string = emoji.emojize(user_input, use_aliases=True)

# Output the emojized version of the string
print(f"Emojized version: {emojized_string}")
