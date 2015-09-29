# Import regular expression module
import re
# Allow any decimal digit
containsNumbers = re.compile('\d')
# Get user input
userInput = input("Please enter a password")
# Print user input
print("Your entered password was: "+userInput)

# Get string length
strLen = len(userInput)

# If string length is less than 8
if(strLen < 8):
    print("Password is too short, which is bad.")
else:
    # If the entire string is lower case
    if(userInput.islower()):
        print("Password is bad, please add capitalized letters.")
    # If the string contains a number, return value as boolean(t/f)
    elif(bool(containsNumbers)):
        print("Great password!")
        validPassword = True
    else:
    # If the string didn't contain a capitalized letter AND number
        print("Please add capitalized letters, numbers and some stupid characters.")


