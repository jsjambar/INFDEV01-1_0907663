﻿userInput = input("Please enter the text you wish to get returned backwards.")
# Gives the reverse value back.
# [start:end:steps]
# We dont enter a start and end value, so we grab the entire string.
# By using -1 we go 1 step back and get the string in a reversed way.
reversedInput = userInput[::-1]

print(reversedInput)