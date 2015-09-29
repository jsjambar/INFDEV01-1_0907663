# Get string and numbers that we need for the shifting
string = input("Enter the text you want to get shifted.")
number = int(input("Enter the number you want to shift the letters with"))
# Empty string to place the new shifted characters in
newStr = ""

# If number is smaller than 1, there's no point in shifting.. is there?
while(number < 1):
    number = int(input("Enter the number you want to shift the letters with"))

# Loop through every character in the given string.
for char in string:
    # If it's a letter, get the shifted letter.
    if(char.isalpha()):
        # Get ascii integer from the character
        oldCharInt = ord(char)
        # If the character is z, start from a and reduce the number by 1
        # If the character is z and number is 1, we just reset it to the ascii of a
        if(char == 'z'):
            oldCharInt = ord('a')
            if(number > 1):
                newCharInt = oldCharInt + (number - 1)
            else:
                newCharInt = oldCharInt
        else:
            newCharInt = oldCharInt + number

        # Turn the ascii integer into a character string
        newChar = chr(newCharInt)
        # Add the character to the new shifted string
        newStr += newChar

    # Else we re-add the non-letter character.
    else:
        newStr += char

# Print the new shifted string.
print(newStr)