

# Convert time to 24 hours
def convert_to_24_hours(time_24hr):

    # Check for meal times
    if "07:00" <= time_24hr <= "08:00":
        meal = "Breakfast"
    elif "12:00" <= time_24hr <= "13:00":
        meal = "Lunch"
    elif "20:00" <= time_24hr <= "21:00":
        meal = "Dinner"

    # Assuming input format like "HH:mm"
    return time_24hr


time_24hr = "07:00"
result = convert_to_24_hours(time_24hr)
print(result)



# Get user input. Eg: 7:00, 8:00
