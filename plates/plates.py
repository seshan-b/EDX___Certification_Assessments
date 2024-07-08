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
        return False

    # Step 2: Check if the plate starts with at least two letters
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    #Step 3: Check for allowed characters (letters and numbers only)
    for char in plate:
        if not (char.isalpha() or char.isdigit()):
            return False
#     // Step 4: Check the position of numbers
#     number_found = False
#     for i in range(length(plate)):
#         if plate[i].isdigit():
#             number_found = True
#             // Ensure all characters after the first number are also numbers
#             for j in range(i, length(plate)):
#                 if not plate[j].isdigit():
#                     return False
#             break

#     // Step 5: If all checks are passed, return True
#     return True

def main():
    # Example plate to test
    plate = "ABC123"
    # Check if the plate is valid
    result = is_valid_plate(plate)
    # Print the result
    print(f"Is the plate '{plate}' valid? {result}")

# Run the main function
if __name__ == "__main__":
    main()
