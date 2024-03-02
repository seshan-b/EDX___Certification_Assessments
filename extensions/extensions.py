# Importing the mimetypes module for media type guessing
import mimetypes

# Function to get the media type based on the file name
def get_media_type(file_name):
    # List of supported file suffixes
    suffixes = ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']

    # Lowercase
    file_name.lower()

    # Check if the file extension is in the list of supported suffixes
    if file_extension and file_extension in suffixes:
        # Use mimetypes to guess the media type
        media_type, _ = mimetypes.guess_type(file_name)
        # Return the guessed media type or the default if it couldn't be guessed
        if media_type:
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
if __name__ == "__main__":
    main()
