def process_greeting(greeting):
    processed_greeting = greeting.strip().lower()


    if processed_greeting.startswith("hello"):
        return "$0"
    elif processed_greeting.startswith("h"):
        return "$20"
    else:
        return "$100"




def main():
    user_greeting = input("Enter a greeting: ")


# Run
main()



