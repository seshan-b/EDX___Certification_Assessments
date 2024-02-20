# Get input from the user
user_input = input("Enter a text with emoticons: ")

# Use the print function with the sep argument to replace emoticons with emojis
print(user_input.replace(":)", "😊").replace(":(", "😞"), sep="")
