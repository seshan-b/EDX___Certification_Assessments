import os
import magic

# Get the user input


# Create a function to get the file media type
def get_media_type(file_name):
    file_path = os.path.abspath(file_name)
    mime = magic.Magic()
    media_type = mime.from_file(file_path)
    return media_type



print(get _media_type('ima.jpg'))

# output the file media type
