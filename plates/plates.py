# ### 1st go at the code
# ### Breaking down the problem
# # All vanity plates must start with at least two letters.
# # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# # Numbers cannot be used in the middle of a plate, they must come at the end.
# # Eg: AAA222 would be an acceptable
# # Eg: AAA22A would not be acceptable
# # No periods, spaces, or punctuation marks are allowed.


# def is_valid_plate(plate):
#     # Step 1: Check the length of the plate
#     if len(plate) < 2 or len(plate) > 6:
#         return False

#     # Step 2: Check if the plate starts with at least two letters
#     if not (plate[0].isalpha() and plate[1].isalpha()):
#         return False

#     # Step 3: Check for allowed characters (letters and numbers only)
#     for char in plate:
#         if not (char.isalpha() or char.isdigit()):
#             return False

#     # Step 4: Check the position of numbers
#     number_started = False
#     for i in range(len(plate)):
#         if plate[i].isdigit():
#             number_started = True
#             # If the first number is '0', it's invalid
#             if i > 0 and plate[i] == '0' and plate[i-1].isalpha():
#                 return False
#             # Ensure all characters after the first number are also numbers
#             for j in range(i, len(plate)):
#                 if not plate[j].isdigit():
#                     return False
#             break
#         elif number_started and plate[i].isalpha():
#             # Invalid if we encounter a letter after the numbers have started
#             return False

#     # If all checks are passed, return True
#     return True

# def main():
#     # Prompt the user for input
#     plate = input("Enter the vanity plate: ")
#     # Check if the plate is valid
#     result = is_valid_plate(plate)
#     # Print the result
#     if result:
#         print("Valid")
#     else:
#         print("Invalid")

# # Run the main function
# if __name__ == "__main__":
#     main()


########################################################################################################

# ### Refined version
### Breaking down the problem
# All vanity plates must start with at least two letters.
# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# Numbers cannot be used in the middle of a plate; they must come at the end.
# Eg: AAA222 would be acceptable
# Eg: AAA22A would not be acceptable
# No periods, spaces, or punctuation marks are allowed.

def is_valid_plate(plate):
    # Step 1: Check the length of the plate
    if not 2 <= len(plate) <= 6:
        return False

    # Step 2: Check if the plate starts with at least two letters
    if not (plate[:2].isalpha()):
        return False

    # Step 3: Check for allowed characters and correct positioning of numbers
    for i, char in enumerate(plate):
        if char.isdigit():
            # If the first number is '0', it's invalid
            if char == '0' and i == 2:
                return False
            # Ensure all characters after the first number are also numbers
            if not plate[i:].isdigit():
                return False
            break
        elif not char.isalpha():
            return False

    # If all checks are passed, return True
    return True

def main():
    # Prompt the user for input
    plate = input("Enter the vanity plate: ")
    # Check if the plate is valid
    result = is_valid_plate(plate)
    # Print the result
    print("Valid" if result else "Invalid")

# Run the main function
if __name__ == "__main__":
    main()

