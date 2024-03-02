# Importing the mimetypes module for media type guessing
import mimetypes

# Function to get the media type based on the file name
def get_media_type(file_name):
    # List of supported file suffixes
    suffixes = ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']

    # Check if the file name has a dot (.) and get the lowercase file extension
    if '.' in file_name:
        file_extension = file_name.split('.')[-1].lower()
    else:
        file_extension = None  # If there's no dot in the file name, set file_extension to None

    # Check if the file extension is in the list of supported suffixes
    if file_extension and file_extension in suffixes:
        # Use mimetypes to guess the media type
        media_type, _ = mimetypes.guess_type(file_name)
        # Return the guessed media type or a default if it couldn't be guessed
        if media_type:
            print(media_type)
            return media_type
        else:
            return 'Unknown media type'
    else:
        # If the file has an unsupported or no suffix, return the default media type
        return 'Unsupported file type'

# Main function to run the program
def main():
    # Prompt the user for the file name
    file_name = input("Enter the name of the file: ")

    # Get and print the media type
    media_type = get_media_type(file_name)
    print(f"The media type of the file is: {media_type}")

# Run the program only if this script is executed directly (not imported as a module)
main()
