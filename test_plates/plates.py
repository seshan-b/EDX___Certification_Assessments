# def main():
#     # Prompt the user for input
#     plate = input("Enter the vanity plate: ")
#     # Check if the plate is valid
#     try:
#         result = is_valid(plate)
#         # Print the result
#         print("Valid" if result else "Invalid")
#     except ValueError as e:
#         print(f"Error: {e}")

# def is_valid(s):
#     # Step 1: Check the length of the plate
#     if not 2 <= len(s) <= 6:
#         return False

#     # Step 2: Check if the plate starts with at least two letters
#     if not s[:2].isalpha():
#         return False

#     # Step 3: Check for allowed characters and correct positioning of numbers
#     number_started = False  # Flag to check when numbers start
#     for i, char in enumerate(s):
#         if char.isdigit():
#             if char == '0' and not number_started and i > 1:
#                 return False
#             number_started = True  # Once a digit is found, set this flag
#         elif char.isalpha():
#             if number_started:
#                 return False  # If a letter comes after numbers have started, it's invalid
#         else:
#             return False  # Any non-alphabetic and non-digit character makes the plate invalid

#     return True



# if __name__ == "__main__":
#     main()


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the length is between 2 and 6 characters
    if not 2 <= len(s) <= 6:
        return False

    # Check if the plate starts with at least two letters
    if not s[:2].isalpha():
        return False

    # Check if the plate contains only alphanumeric characters
    if not s.isalnum():
        return False

    # Check the positioning of numbers
    for i, char in enumerate(s):
        if char.isdigit():
            index = s.index(char)
            if s[index:].isdigit() and int(char) != 0:
                return True
            else:
                return False

    # If no numbers or other issues, return True if the plate is valid
    return True

if __name__ == "__main__":
    main()
