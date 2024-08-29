def main():
    input_string = input("Please enter a string: ")
    result_string = shorten(input_string)
    print(result_string)

def shorten(word):
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    result_string = "".join([char for char in word if char not in vowels])

    # Simulate error condition (e.g., removing punctuation, etc.)
    if "," in word or "!" in word:  # Example condition
        print("Error: Punctuation mishandled")
        exit(1)  # Exit with error code 1

if __name__ == "__main__":
    main()
