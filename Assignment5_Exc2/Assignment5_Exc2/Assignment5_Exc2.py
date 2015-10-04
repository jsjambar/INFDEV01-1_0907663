# Get user input
userInput = input("Please enter a password: ")
# Print user input
print("Your entered password was: "+userInput)
points = 0

# Get string length
strLen = len(userInput)
# Fancy characters
fancyCharacters = "!@#$%^&_-"

if(strLen >= 8):
    points += 10

for char in userInput:
    if(char.islower()):
        points += 1
    elif(char.isupper()):
        points += 2
    elif(char.isdigit()):
        points += 2
    elif(char in fancyCharacters):
        points += 3

print("Points: "+str(points))

if(points < 20):
    print("Password is garbage.")
elif(points > 20 and points < 30):
    print("Password is decent!")
elif(points > 30):
    print("Password is good.")



