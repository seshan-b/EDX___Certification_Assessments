# Importing the mimetypes module for media type guessing
import mimetypes

# List of supported file suffixes
suffixes = ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']

# Prompt the user for the file name
file_name = input("Enter the name of the file: ")

# Check if the file name has a dot (.) and get the lowercase file extension
if '.' in file_name:
    file_extension = file_name.split('.')[-1].lower()
else:
    file_extension = None  # If there's no dot in the file name, set file_extension to None

media_type = ''

# Check if the file extension is in the list of supported suffixes
if file_extension and file_extension in suffixes:
    # Use mimetypes to guess the media type
    media_type, _ = mimetypes.guess_type(file_name)
    # Print the guessed media type or a default if it couldn't be guessed
    media_type
print(f"The media type of the file is: {media_type}")
