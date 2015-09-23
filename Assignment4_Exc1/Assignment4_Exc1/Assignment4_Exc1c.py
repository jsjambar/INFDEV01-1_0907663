# Get number
value           = input("Enter a number.")

# Let's remove all '-'-characters method
nasty_value     = value.replace("-", "")
# Convert to float
value           = float(value)
# Lazy method
absolute_value  = abs(value)
# Fancy if-statement?


# Convert the floated values to strings
value           = str(value)
absolute_value  = str(absolute_value)

print("Absolute value is:"+value)
print("Lazy non-if method: "+absolute_value)
print("Nasty remove '-' method: "+nasty_value)