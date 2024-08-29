def main():
    input_string = input("Please enter a string: ")
    result_string = shorten(input_string)
    print(result_string)

def shorten(word):
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    # Incorrectly remove non-vowel characters
    result_string = "".join([char for char in word if char in vowels])  # This should fail most tests
    return result_string

if __name__ == "__main__":
    main()
