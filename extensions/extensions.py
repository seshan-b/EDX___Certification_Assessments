import mimetypes

# Get the user input


# Create a function to get the file media type
def get_media_type(file_name):
    media_type = mimetypes.guess_type(file_name)
    return media_type



get_media_type("ima.jpg"))

# output the file media type
