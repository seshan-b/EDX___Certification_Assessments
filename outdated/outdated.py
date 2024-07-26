### Breaking down the problem
# Implement a program that prompts the user for a date, AD (Anno Domini) in month-day-year order.
# It needs to be formatted like this: 9/8/1636 or September 8, 1636.
# The month in the latter might be any of the values in the list below.

# List of month names for conversion
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Function to check if the date format is valid and extract components
def extract_date_components(date_string):
    # Check for numeric date format (e.g., 9/8/1636)
    if date_string.count("/") == 2:
        parts = date_string.split("/")
        # Ensure there are 3 parts, each part is a digit, and the year part has 4 digits
        if len(parts) == 3 and all(part.isdigit() for part in parts) and len(parts[2]) == 4:
            return int(parts[0]), int(parts[1]), int(parts[2])  # Return month, day, year as integers
        else:
            return None, None, None  # Invalid format, return None

    # Check for written date format (e.g., September 8, 1636)
    elif any(month in date_string for month in months):
        if "," not in date_string:  # Ensure there is a comma
            return None, None, None  # Invalid format, return None
        parts = date_string.replace(",", "").split()
        # Ensure there are 3 parts, the day part is a digit, and the year part has 4 digits
        if len(parts) == 3 and parts[1].isdigit() and len(parts[2]) == 4 and parts[2].isdigit():
            month_name = parts[0]
            if month_name in months:
                month = months.index(month_name) + 1  # Convert month name to month number
                return month, int(parts[1]), int(parts[2])  # Return month, day, year as integers
        return None, None, None  # Invalid format, return None

    return None, None, None  # Invalid format, return None

# Loop to reprompt the user until a valid date is entered
while True:
    # Step 1: Prompt the user for input
    date_string = input("Enter a date (e.g., 9/8/1636 or September 8, 1636): ").strip()

    # Extract components and validate the format
    month, day, year = extract_date_components(date_string)

    # If any component is None, it means the input format was invalid
    if month is None or day is None or year is None:
        print("Error: Invalid date format. Please try again.")
        continue  # Reprompt the user for input

    # Step 3: Validate the date
    is_valid = True
    error_message = ""

    # Check if month is between 1 and 12
    if month < 1 or month > 12:
        is_valid = False
        error_message = "Invalid month. Please enter a month between 1 and 12."

    # Check if day is valid for the given month
    # Days in each month (assuming non-leap year for simplicity)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_valid:
        if day < 1 or day > days_in_month[month - 1]:
            is_valid = False
            error_message = f"Invalid day for the given month. Please enter a day between 1 and {days_in_month[month - 1]}."

    # Check if year is a positive number
    if is_valid and year < 1:
        is_valid = False
        error_message = "Invalid year. Please enter a positive number for the year."

    if is_valid:
        # Step 4: Format the date as YYYY-MM-DD
        formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
        print(formatted_date)
        break  # Exit the loop
    else:
        print("Error:", error_message)  # Print the error message and reprompt the user
