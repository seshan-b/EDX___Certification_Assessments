
### Breaking down the problem
# Implement a program that prompts the user for a date, AD (Anno Domini) in month-day-year order
# It needs to be formatted like this 9/8/1636 or September 8, 1636
# Wherein the month in the latter might be any of the values in the list below


# Step 1: Prompt the user for input
date_string = input("Enter a date (e.g., 9/8/1636 or September 8, 1636): ")
# print("You entered:", date_string)


# Step 2: Determine the format of date_string and extract components
month = None
day = None
year = None

# List of month names for conversion
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Check if the date_string contains slashes
if "/" in date_string:
    # Split by "/"
    parts = date_string.split("/")
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
else:
    # Split by spaces and comma
    parts = date_string.replace(",", "").split()
    month_name = parts[0]
    day = int(parts[1])
    year = int(parts[2])
    # Convert month_name to month number
    month = months.index(month_name) + 1

# Print extracted components for verification
# print("Month:", month)
# print("Day:", day)
# print("Year:", year)
