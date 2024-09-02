def value(greeting):
    processed_greeting = greeting.strip().lower()

    if processed_greeting.startswith("hello"):
        return "$0"
    elif processed_greeting.startswith("h"):
        return "$20"
    else:
        return "$100"


def main():
    user_greeting = input("Enter a greeting: ")

    # Display Amount
    result = value(user_greeting)
    print(result)


if __name__ == "__main__":
    main()
