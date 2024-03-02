import mimetypes


# Create a function to get the file media type
def get_media_type(file_name):

    # The underscore is to get 1st part of array
    media_type, _ = mimetypes.guess_type(file_name)lower().trim()
    return media_type




def main():
    user_input = str(input("Enter the file name: "))
    result = get_media_type(user_input)


    # output the file media type
    if result:
        print(result)
    else:
        print(f"Unable to determine the media type for {user_input}")


main()

# Get the user input

