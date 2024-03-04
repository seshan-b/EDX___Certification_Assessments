def camel_to_snake(camel_case):
    snake_case = ''

    for each_character in camel_case:
        if each_character.isupper():
            snake_case += '_' + each_character.lower()
        else:
            snake_case += each_character

    return snake_case

def main():
    user_input = str(input("Give a name: "))

    process = camel_to_snake(user_input)

    print(process.lower(), end="")


main()
