# ### Breaking down the problem
# Expects zero or two command-line arguments Prompts the user for a str of text.
# Zero if the user would like to output text in a random font. Two if the user would like to output text in a specific font,
# If this is the case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# The program should exit via sys.exit with an error message if first is not -f or --font or the second is not the name of a font.
# Outputs that text in the desired font.


import sys
import random
import pyfiglet

def main():
    # Step 1: Parse Command-Line Arguments
    args = sys.argv[1:]

    # Step 2: Validate Arguments
    if len(args) == 0:
        # No arguments provided, proceed to use a random font
        font = get_random_font()
    elif len(args) == 2:
        if args[0] in ['-f', '--font']:
            font = args[1]  # Get the specified font
            if not validate_font(font):
                sys.exit(f"Error: '{font}' is not a valid font name.")
        else:
            sys.exit("Error: First argument must be '-f' or '--font'.")
    else:
        sys.exit("Error: Program expects either zero or two arguments.")

    # Step 3: Prompt for Text Input
    text = input("Enter the text you want to display: ")

    # Step 4: Output the Text in the Desired or Random Font
    output_text_in_font(text, font)

def get_random_font():
    # Get a list of available fonts from pyfiglet
    fonts = pyfiglet.FigletFont.getFonts()
    return random.choice(fonts)

def validate_font(font_name):
    # Validate if the font is available in pyfiglet
    return font_name in pyfiglet.FigletFont.getFonts()

def output_text_in_font(text, font):
    # Use pyfiglet to render the text in the specified font
    figlet = pyfiglet.Figlet(font=font)
    rendered_text = figlet.renderText(text)
    print(rendered_text)

if __name__ == "__main__":
    main()
