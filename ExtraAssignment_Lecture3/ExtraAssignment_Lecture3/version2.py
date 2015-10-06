for index in range(0,5):

    # lets place the current amount of stars in a string
    stars_string = '*' * (5 - index)
    stars_string += (' ' * index) + '*'

    if index == 4:
        stars_string = '*' * (index+2)

    print(stars_string)
