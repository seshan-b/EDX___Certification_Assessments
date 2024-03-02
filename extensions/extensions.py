import mimetypes


# Create a function to get the file media type
def get_media_type(file_name):


    file_name.strip().lower()

    # The underscore is to get 1st part of array
    media_type, _ = mimetypes.guess_type(file_name)
    return media_type




def main():

    # Get the user input Clean data on input
    user_input = str(input("Enter the file name: "))
    if '.' in user_input:

        result = get_media_type(user_input)
        print(result)
        # print(user_input)
    else:
        print("application/octet-stream")


main()



