def snake_case(input_string):
    # Use the replace method to replace spaces with underscores

    for i in result_string:

        result_string = input_string.replace(' ', '_').lower()
        print(result, end="")
    return result_string


def main():
    user_input = str(input("Give a name: "))

    process = snake_case(user_input)

    print(process)


main()
