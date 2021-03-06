﻿import math
height          = int(input("What should be the height of the figures? "))
width           = int(input("What should be the width of the figures? "))
figureString    = ""

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

    # We do (height - 1) because the loop ends at index (height - 1).
    # We check if we're at the first index or at the last and just create the entire width of the cube at the top and bottom
    # Else we check if we're at the first or last index of the width and add a star there.
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
    for x_width in range(0, (x + 1)):
        figureString += "*"

    figureString += "\n"

print(figureString)
figureString = ""


# A full isosceles triangle
print("A full isosceles triangle.")

for y in range(1, height):
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
    for space in range(0, spaces):
        figureString += " "

    for star in range(0, stars):
        figureString += "*"

    figureString += "\n"

print(figureString)
figureString = ""


# A full circle.
print("A full circle.")

# Center
center = width / 2

for y in range(0, width):
    # Get the distance between the center and current index (y)
    distance_y = (center - y) * (center - y)
    for x in range(0, width):
        # Get the distance between the center and the current index (x)
        distance_x = (center - x) * (center - x)
        # Calculate the total distance by adding the y-axis and x-axis distance and using the square root on this (because we did value * 2 on distance_y and distance_x)
        distance = math.sqrt(distance_y + distance_x)
        #print(center)
        #print(distance)
        # If the center is bigger than the distance, we can draw asterisk
        if(distance < center): 
            figureString += "*"
        else:
            figureString += " "
        

    figureString += "\n"

print(figureString)
figureString = ""

# A full circle.
print("A beautiful face.")

# Center
center = width / 2

for y in range(0, width):
    # Get the distance between the center and current index (y)
    distance_y = (center - y) * (center - y)
    for x in range(0, width):
        # Get the distance between the center and the current index (x)
        distance_x = (center - x) * (center - x)
        # Calculate the total distance by adding the y-axis and x-axis distance and using the square root on this (because we did value * 2 on distance_y and distance_x)
        distance = math.sqrt(distance_y + distance_x)

        # distance = 0 = center and thats for the nose
        if(distance == 0):
            figureString += "#"
        # eyes
        elif(distance == 5 and y == (center - 3)):
            figureString += "o"
        # smiley
        elif(distance == 5 and y > center):
            figureString += "-"
        # face smiley
        elif(distance < center and distance > (center / 1.2)): 
            figureString += "*"
        else:
            figureString += " "
        

    figureString += "\n"

print(figureString)
figureString = ""