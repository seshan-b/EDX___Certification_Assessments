# Importing the mimetypes module for media type guessing
import mimetypes

# Function to get the media type based on the file name
def get_media_type(file_name):
    # List of supported file suffixes
    suffixes = ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']

    # Lowercase
    get_media = file_name.lower()

    get_media = mimetypes.guess_type(file_name)

    print(get_media)

    return get_media


print(get_media_type("image/jpeg"))


# Main function to run the program
# def main():
#     Prompt the user for the file name
#     file_name = input("Enter the name of the file: ")

#     Get and print the media type
#     media_type = get_media_type(file_name)
#     print(f"The media type of the file is: {media_type}")

# Run the program only if this script is executed directly (not imported as a module)
# if __name__ == "__main__":
#     main()
