def main():
    input_string = input("Please enter a string: ")
    result_string = shorten(input_string)
    print(result_string)

def shorten(word):
    # Set of vowels to remove
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    # Use a list comprehension to filter out vowels
    result_string = "".join([char for char in word if char not in vowels])
    return result_string

if __name__ == "__main__":
    main()
