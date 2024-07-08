### Breaking down the problem
# All vanity plates must start with at least two letters.
# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# Numbers cannot be used in the middle of a plate, they must come at the end.
# Eg: AAA222 would be an acceptable
# Eg: AAA22A would not be acceptable
# No periods, spaces, or punctuation marks are allowed.


def is_valid_plate(plate):
    # Step 1: Check the length of the plate
    if len(plate) < 2 or len(plate) > 6:
        return "Invalid"

    # Step 2: Check if the plate starts with at least two letters
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return "Invalid"

    #Step 3: Check for allowed characters (letters and numbers only)
    for char in plate:
        if not (char.isalpha() or char.isdigit()):
            return "Invalid"
    # Step 4: Check the position of numbers
    for i in range(len(plate)):
        if plate[i].isdigit():
            # Ensure all characters after the first number are also numbers
            for j in range(i, len(plate)):
                if not plate[j].isdigit():
                    return "Invalid"
            break
        return "Valid"

    # Step 5: If all checks are passed, return True
    return "Valid"

def main():
    # Prompt the user for input
    plate = input("Enter the vanity plate: ")
    # Check if the plate is valid
    result = is_valid_plate(plate)
    # Print the result
    print(f"{result}")

# Run the main function
if __name__ == "__main__":
    main()
