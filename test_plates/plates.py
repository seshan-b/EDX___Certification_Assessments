def main():
    # Prompt the user for input
    plate = input("Enter the vanity plate: ")
    # Check if the plate is valid
    try:
        result = is_valid(plate)
        # Print the result
        print("Valid" if result else "Invalid")
    except ValueError as e:
        print(f"Error: {e}")

def is_valid(s):
    # Step 1: Check the length of the plate
    # if not 2 <= len(s) <= 6:
    #     return False

    # Step 2: Check if the plate starts with at least two letters
    # if not (s[:2].isalpha()):
    #     raise ValueError("Plate must start with at least two alphabetic characters.")

    # Step 3: Check for allowed characters and correct positioning of numbers
    for i, char in enumerate(s):
        if char.isdigit():
            # If the first number is '0', it's invalid
            if char == '0' and i == 2:
                return False
            # Ensure all characters after the first number are also numbers
            if not s[i:].isdigit():
                return False
            break
        elif not char.isalpha():
            return False

    # If all checks are passed, return True
    return True


if __name__ == "__main__":
    main()
