
### Breaking down the problem
# Implement a program that prompts the user for a date, AD (Anno Domini) in month-day-year order
# It needs to be formatted like this 9/8/1636 or September 8, 1636
# Wherein the month in the latter might be any of the values in the list below


# Step 1: Prompt the user for input
date_input = input("Please enter a date (e.g., 9/8/1636 or September 8, 1636): ")

# Step 2: Validate the input
def validate_date(date_str):
    # Check for "month/day/year" format
    if '/' in date_str:
        parts = date_str.split('/')
        if len(parts) == 3:
            month, day, year = parts
            if month.isdigit() and day.isdigit() and year.isdigit():
                return 'numeric'

    # Check for "Month day, year" format
    elif ' ' in date_str and ',' in date_str:
        parts = date_str.split(' ')
        if len(parts) == 3:
            month, day_year = parts[0], parts[1] + parts[2]
            if day_year.replace(',', '').isdigit():
                return 'textual'

    return 'invalid'

date_format = validate_date(date_input)

if date_format == 'invalid':
    print("Invalid date format. Please try again.")
else:
    print(f"Valid date format: {date_format}")

# Step 3: Parse the date
def parse_date(date_str, date_format):
    if date_format == 'numeric':
        month, day, year = date_str.split('/')
        return int(year), int(month), int(day)
    elif date_format == 'textual':
        month_names = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }
        parts = date_str.split(' ')
        month = month_names[parts[0]]
        day = int(parts[1].replace(',', ''))
        year = int(parts[2])
        return year, month, day

if date_format != 'invalid':
    year, month, day = parse_date(date_input, date_format)
    print(f"{year}, Month={month}, Day={day}")

# Step 4: Reformat the date
def reformat_date(year, month, day):
    return f"{year:04d}-{month:02d}-{day:02d}"

if date_format != 'invalid':
    formatted_date = reformat_date(year, month, day)
    print(f"Formatted date: {formatted_date}")
