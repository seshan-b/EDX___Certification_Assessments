# Importing the mimetypes module for media type guessing
import mimetypes

# Function to get the media type based on the file name
def get_media_type(file_name):
    # List of supported file suffixes
    suffixes = ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']

    # Check if the file name has a dot (.) and get the lowercase file extension
    file_extension = file_name.split('.')[-1].lower()


    # Check if the file extension is in the list of supported suffixes
    if file_extension and file_extension in suffixes:
        # Use mimetypes to guess the media type
        media_type, _ = mimetypes.guess_type(file_name)
        print(media_type)
        # Return the guessed media type or a default if it couldn't be guessed
        return media_type


# Main function to run the program
def main():
    # Prompt the user for the file name
    file_name = str(input("Enter the name of the file: "))
    print(file_name)

    # Get and print the media type
    media_type = get_media_type(file_name)
    print(f"The media type of the file is: {media_type}")

# Run the program only if this script is executed directly (not imported as a module)
main()
