# Standard values
# amount_of_pixels is the amount of times (+1) it has to loop and go down.
# amount_of_stars is the amount of stars it has to make per line
amount_of_pixels = 4
amount_of_stars = 5

# for loop for the amount of lines
for index in range(0,amount_of_pixels):

    # for loop for the amount of stars
    for stars in range(0,amount_of_stars):

        # lets place the current amount of stars in a string
        stars_string = '*' * amount_of_stars
        # do a minus one so we can create the triangle
        amount_of_stars = amount_of_stars - 1
        # variable so that we know how many times we need an empty space
        amount_of_spaces = amount_of_pixels - amount_of_stars

        # for loop to make the amount of spaces
        for spaces in range(0, amount_of_spaces):
            stars_string += ' '

        stars_string += '*'

        if amount_of_stars == 0:
            amount_of_pixels = amount_of_pixels + 2
            stars_string = '*' * amount_of_pixels

        print(stars_string)
