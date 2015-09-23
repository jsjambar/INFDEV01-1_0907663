# Get number
celsius     = input("What number do you want to convert?")
# Convert to float
celsius     = float(celsius)
# Formula for Celsius to Kelvin is celsius + 273.15
kelvin      = celsius + 273.15

# Kelvin keeps getting updated in this while, so if it's below 0 after the first time it keeps running till it is above 0
while(kelvin < 0):
    celsius  = input("This is below absolute zero. Please enter another number.")
    kelvin   = float(celsius) + 273.15

# Convert back to strings to show in a print
celsius     = str(celsius)
kelvin      = str(kelvin)
# Print the string with fahrenheit to celsius convertion
print(celsius + " celsius is " +kelvin+ " Kelvin")

