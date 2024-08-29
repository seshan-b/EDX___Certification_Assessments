def main():
    input_string = input("Please enter a string: ")
    result_string = shorten(input_string)
    print(result_string)

def shorten(word):
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    print(f"Original word: {word}")  # Debug print
    result_string = "".join([char for char in word if char not in vowels])
    print(f"Result string: {result_string}")  # Debug print
    return result_string

if __name__ == "__main__":
    main()
