def camel_to_snake(camel_case):
    # Initialize an empty string to store the snake_case version
    snake_case = ''

    # Iterate through each character in the camel_case string
    for each_character in camel_case:
        # Check if the character is uppercase
        if each_character.isupper():
            # If uppercase, add an underscore and the lowercase version of the character to snake_case
            snake_case += '_' + each_character.lower()
        else:
            # If not uppercase, add the character unchanged to snake_case
            snake_case += each_character

    # Return the resulting snake_case string
    return snake_case.strip()

def main():
    # Prompt the user for input and store it in the user_input variable
    user_input = str(input("Give a name: "))

    # Call the camel_to_snake function with the user input and store the result in the process variable
    process = camel_to_snake(user_input)

    # Print the snake_case version of the input in lowercase without a new line
    print(process.lower(), end="")

# Call the main function to execute the program
main()
