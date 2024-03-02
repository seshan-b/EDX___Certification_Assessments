

# Convert time to 24 hours
def convert_to_24_hours(time_in_24hr):

    # Convert time to decimal representation
    hours, minutes = map(int, time_in_24hr.split(':'))
    time_decimal = round(hours + minutes / 60.0)

    print(time_decimal)
    return time_decimal

time_24hr = "12:01"

result = convert_to_24_hours(time_24hr)






def main:
    # Get user input. Eg: 7:00, 8:00
    user_input = str(input("Get the time (Eg: 7:00): "))

    time_in_24hr = user_input

    # Check for meal times
    if "07:00" <= time_in_24hr <= "08:00":
        meal_type = "Breakfast"
    elif "12:00" <= time_in_24hr <= "13:00":
        meal_type = "Lunch"
    elif "20:00" <= time_in_24hr <= "21:00":
        meal_type = "Dinner"
    else:
        meal_type = "No time given"
    print(time_in_24hr)
    print(meal_type)


main()
