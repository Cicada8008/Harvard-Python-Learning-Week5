import sys
import random
from pyfiglet import Figlet

# Check if a font is provided with the `-f` flag
if len(sys.argv) >= 3 and sys.argv[1] == "-f":
    font_name = sys.argv[2]
else:
    print("Invalid usage: Please specify a font using the -f flag (e.g., `python3 figlet.py -f slant`)")
    sys.exit(1)

figlet = Figlet()

# Set the font if available, otherwise exit with an error message
if font_name in figlet.getFonts():
    figlet.setFont(font=font_name)
else:
    print("Invalid usage: Specified font not found.")
    sys.exit(1)

# Prompt the user for the text to render
wordy = input("Enter the text you want to render: ")

# Render the text and print it
print(figlet.renderText(wordy))
