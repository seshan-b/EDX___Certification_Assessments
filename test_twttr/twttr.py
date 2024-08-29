def main():
    # Prompt the user to enter a string and store it in a variable called 'input_string'
    input_string = input("Please enter a string: ")

    # Call the 'shorten' function to remove vowels from the input string
    result_string = shorten(input_string)

    # Print the resulting string without vowels
    print(result_string)


def shorten(word):
    # Define a set of vowels: {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}

    # Initialize an empty string to store the result
    result_string = ""

    # For each character in the input word:
    for char in word:
        # If the character is not a vowel, append it to the result string
        if char not in vowels:
            result_string += char

    # Return the resulting string without vowels
    return result_string


if __name__ == "__main__":
    main()
