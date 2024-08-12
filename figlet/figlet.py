# ### Breaking down the problem
# Expects zero or two command-line arguments Prompts the user for a str of text.
# Zero if the user would like to output text in a random font. Two if the user would like to output text in a specific font,
# If this is the case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# The program should exit via sys.exit with an error message if first is not -f or --font or the second is not the name of a font.
# Outputs that text in the desired font.

import sys
import random
import pyfiglet

args = sys.argv[1:]

# Determine the font to use
if len(args) == 0:
    font = random.choice(pyfiglet.FigletFont.getFonts())
elif len(args) == 2 and args[0] in ['-f', '--font']:
    font = args[1]
    if font not in pyfiglet.FigletFont.getFonts():
        sys.exit(f"Error: '{font}' is not a valid font name.")
else:
    sys.exit("Error: Program expects either zero or two arguments with the first being '-f' or '--font'.")

# Prompt for text input
text = input("Enter the text you want to display: ")

# Output the text in the selected font
print(pyfiglet.Figlet(font=font).renderText(text))
