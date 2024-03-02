

# Convert time to 24 hours
def convert_to_24_hours(time_24hr):

    # Convert time to decimal representation
    hours, minutes = map(int, time_24hr.split(':'))
    time_decimal = hours + minutes / 60.0

    print(time_decimal.rou)
    return time_decimal

time_24hr = "12:01"

result = convert_to_24_hours(time_24hr)


# Check for meal times
if "07:00" <= time_24hr <= "08:00":
    meal = "Breakfast"
elif "12:00" <= time_24hr <= "13:00":
    meal = "Lunch"
elif "20:00" <= time_24hr <= "21:00":
    meal = "Dinner"
else:
    meal = "No time given"

print(meal)



# Get user input. Eg: 7:00, 8:00
