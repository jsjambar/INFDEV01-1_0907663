height          = int(input("What should be the height of the figures? "))
width           = int(input("What should be the width of the figures? "))
figureString    = ""

'''
# A full square
print("A full square.")

for y in range(0, height):

    for x in range(0, width):
        figureString += "*"
    figureString += "\n"

print(figureString)
figureString = ""

# A hollow square
print("A hollow square.")

for y in range(0, height):

    if (y == 0 or y == (height - 1) ):
        for x in range(0, width):
            figureString += "*"
    else:
        for x in range(0, width):
            if (x == 0 or x == (width - 1) ):
                figureString += "*"
            else:
                figureString += " "

    figureString += "\n"



print(figureString)
figureString = ""

# A full rectangle triangle
print("A full rectangle triangle.")


for x in range(0, width):
 
    # x + 1 causes the x to get increased by 1, which means that we get no space at the first line and we still get 5 stars at the bottom!
    for x_width in range(0, (x+1)):
        figureString += "*"

    figureString += "\n"

print(figureString)
figureString = ""


# A full isosceles triangle
print("A full isosceles triangle.")

for y in range(0, height):
    # Spaces = width - current index. This way we know how many spaces we need before the stars
    spaces = height - y
    # Stars = width - spaces. We removed the amount of spaces we have, so we know how many stars we need to show.
    # After we know how many stars, we need to add stars AFTER the centered line, we do this by removing 1 from the index and adding this
    # to the star amount.
    stars  = (height - spaces) + (y - 1)

    #print("y = "+str(y))
    #print("spaces = "+str(spaces))
    #print("stars = "+str(stars))

    # So we don't get the first empty line cause of index 0
    if(y > 0):

        for space in range(0, spaces):
            figureString += " "

        for star in range(0, stars):
            figureString += "*"

        figureString += "\n"

print(figureString)
figureString = ""
'''


# A full circle.
print("A full circle.")

for y in range(0, height):



    figureString += "\n"

print(figureString)
figureString = ""


'''
# Ugly face.
for y in range(0, 10):
    for x in range(0, 10):
        if((y == 0 or y == 8) and x > 3 and x < 7):
            figureString += "*"
        elif((y == 1 or y == 7) and (x == 3 or x == 7)):
            figureString += "*"
        elif((y == 2 or y == 6) and (x == 2 or x == 8)):
            figureString += "*"
        # Eyebrows
        elif(y == 2 and (x == 3 or x == 7)):
            figureString += "_"
        elif((y == 3 or y == 4 or y == 5) and (x == 1 or x == 9)):
            figureString += "*"
        # Eyes
        elif(y == 3 and (x == 3 or x == 7)):
            figureString += "o"
        # Upper part of mouth
        elif(y == 5 and x == 3):
            # \\ because we use the first \ to escape the character '\' itself.
            figureString += "\\"
        elif(y == 5 and x == 5):
            figureString += "#"
        elif(y == 5 and x == 7):
            figureString += "/"
        # Lower part of mouth
        elif(y == 6 and (x == 4 or x == 5 or x == 6)):
             figureString += "-"
        else:
            figureString += " "

    figureString += "\n"

print(figureString)
'''