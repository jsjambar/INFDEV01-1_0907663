# Get number
fahrenheit = input("What number do you want to convert?")
# Convert to integer
fahrenheit  = float(fahrenheit)
# Formula for Fahrenheit to Celsius = (fahrenheit - 32) * 5/9
celsius     = round((fahrenheit - 32) * 5/9, 2)
# Convert back to strings to show in a print
celsius     = str(celsius)
fahrenheit  = str(fahrenheit)
# Print the string with fahrenheit to celsius convertion
print(fahrenheit + " fahrenheit is " +celsius+ " celsius")
