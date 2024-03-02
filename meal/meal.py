

# Convert time to 24 hours
def convert_to_24_hours(time_in_24hr):

    # Convert time to decimal representation
    hours, minutes = map(int, time_in_24hr.split(':'))
    time_decimal = round(hours + minutes / 60.0, 2)

    print(time_decimal)
    return time_decimal




def main():
    # Get user input. Eg: 7:00, 8:00
    user_input = str(input("Get the time (Eg: 7:00): "))

    time_in_24hr = convert_to_24_hours(user_input)

    print(time_in_24hr)

    # # Check for meal times
    # # Check for meal times
    # if 7.0 <= time_in_24hr < 8.0:
    #     meal_type = "Breakfast"
    # elif 12.0 <= time_in_24hr < 13.0:
    #     meal_type = "Lunch"
    # elif 20.0 <= time_in_24hr < 21.0:
    #     meal_type = "Dinner"
    # else:
    #     meal_type = "No time given"

    # print(meal_type)
    return(time_in_24hr)

main()
