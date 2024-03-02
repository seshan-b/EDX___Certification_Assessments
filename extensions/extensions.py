import mimetypes


# Create a function to get the file media type
def get_media_type(file_name):


    # clean data
    file_name.lower()

    # The underscore is to get 1st part of array
    media_type, _ = mimetypes.guess_type(file_name)
    return media_type




def main():
    user_input = str(input("Enter the file name: "))
    if '.' in user_input:

        result = get_media_type(user_input).strip()
        print(result)
    else:
        print("application/octet-stream")


main()

# Get the user input

