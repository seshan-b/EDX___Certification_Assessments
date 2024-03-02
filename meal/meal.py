# Convert time to 24 hours
def convert(time):
    # Convert time to decimal representation
    hours, minutes = map(int, time.split(':'))
    print(hours)
    time_decimal = round(hours + minutes / 60.0, 2)

    # print(time_decimal)
    return time_decimal


def main():
    # Get user input. Eg: 07:00, 8:00
    user_input = str(input("Get the time (Eg: 7:00): "))

    time = convert(user_input)

    # print(time)

    # Check for meal times
    if 7.0 <= time <= 8.0:
        meal_type = "breakfast time"
    elif 12.0 <= time <= 13.0:
        meal_type = "lunch time"
    elif 18.0 <= time <= 19.0:
        meal_type = "dinner time"
    else:
        meal_type = "No time given"

    print(meal_type)

# Call the main function
if __name__ == "__main__":
    main()
