userInput = input("Please enter the text you wish to get returned backwards.")

newString = ""

for char in userInput:
    newString = char + newString

print(newString)
