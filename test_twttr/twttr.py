import sys

def shorten(word):
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    result_string = "".join([char for char in word if char not in vowels])

    # Simulate an error condition if the word contains punctuation
    if any(char in word for char in ",.!") and result_string != word:
        print("Error: Punctuation mishandled")
        sys.exit(1)  # Exit with error code 1

    return result_string

if __name__ == "__main__":
    input_string = input("Please enter a string: ")
    result_string = shorten(input_string)
    print(result_string)
