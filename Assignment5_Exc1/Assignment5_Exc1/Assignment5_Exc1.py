userInput = input("Please enter the text you wish to get returned backwards.")
# Gives the reverse value back.
# If we were to use [::5], it would return us the values with the index 5
# Using - we get the reversed value returned.
# When you use 1, you get every letter with the index 1, which is everything.
# Combine - for the reversed value and 1 to get everything, leads to getting the entire value returned backwards.
reversedInput = userInput[::-1]

print(reversedInput)