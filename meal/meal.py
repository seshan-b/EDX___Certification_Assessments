

# Convert time to 24 hours
import datetime

def convert_to_24_hours(time_12hr):
    # Assuming input format like "hh:mm"
    time_24hr = datetime.datetime.strptime(time_12hr, "%I:%M").strftime("%H:%M")
    return time_24hr

# Example usage:
time_12hr = "9:00"
result = convert_to_24_hours(time_12hr)
print(result)

time_12hr = "01:00"
result = convert_to_24_hours(time_12hr)
print(result)



# Get user input. Eg: 7:00, 8:00
