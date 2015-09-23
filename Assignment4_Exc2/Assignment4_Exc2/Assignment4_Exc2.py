# Basic values
valid   = False;
options = ['rock', 'paper', 'scissors', 'spock', 'lizard']
win_1   = "Player 1 wins."
win_2   = "Player 2 wins."


# While the right values haven't been entered, keep asking for them to enter rock, paper or scissors.
while(valid == False):
    user_1 = input("Player 1, please enter rock, paper or scissors.").lower()
    user_2 = input("Player 2, please enter rock, paper or scissors.").lower()

    if( (user_1 in options) & (user_2 in options) ):
        valid = True;

# If a right value was entered..
if(valid == True):
    if( (user_1 == 'rock' and user_2 == 'rock')             | 
        (user_1 == 'paper' and user_2 == 'paper')           | 
        (user_1 == 'scissors' and user_2 == 'scissors')     | 
        (user_1 == 'spock' and user_2 == 'spock')           |
        (user_1 == 'lizard' and user_2 == 'lizard') ):
        print("Tied, because both players picked "+user_1)
    else:

        if( user_1 == 'rock' and user_2 == 'paper' ):
            print("Paper covers rock.")
            print(win_2)
        elif( user_1 == 'paper' and user_2 == 'rock'):
            print("Paper covers rock.")
            print(win_1)

        if( user_1 == 'paper' and user_2 == 'scissors' ):
            print("Scissors cuts paper.")
            print(win_2)
        elif( user_1 == 'scissors' and user_2 == 'paper' ):
            print("Scissors cuts paper.")
            print(win_1)

        if( user_1 == 'lizard' and user_2 == 'rock' ):
            print("Rock crushes lizard.")
            print(win_2)
        elif( user_1 == 'rock' and user_2 == 'lizard' ):
            print("Rock crushes lizard.")
            print(win_1)

        if( user_1 == 'spock' and user_2 == 'lizard' ):
            print("Lizard poisons Spock.")
            print(win_2)
        elif( user_1 == 'spock' and user_2 == 'lizard' ):
            print("Lizard poisons Spock.")
            print(win_1)

        if( user_1 == 'scissors' and user_2 == 'spock' ):
            print("Spock smashes scissors.")
            print(win_2)
        elif( user_1 == 'spock' and user_2 == 'scissors' ):
            print("Spock smashes scissors.")
            print(win_1)

        if( user_1 == 'lizard' and user_2 == 'scissors' ):
            print("Scissors decapitates lizard.")
            print(win_2)
        elif( user_1 == 'scissors' and user_2 == 'lizard' ):
            print("Scissors decapitates lizard.")
            print(win_1)

        if( user_1 == 'paper' and user_2 == 'lizard' ):
            print("Lizard eats paper.")
            print(win_2)
        elif( user_1 == 'paper' and user_2 == 'lizard' ):
            print("Lizard eats paper.")
            print(win_1)

        if( user_1 == 'spock' and user_2 == 'paper' ):
            print("Paper disproves spock.")
            print(win_2)
        elif( user_1 == 'paper' and user_2 == 'spock' ):
            print("Paper disproves spock.")
            print(win_1)

        if( user_1 == 'rock' and user_2 == 'spock' ):
            print("Spock vaporizes rock.")
            print(win_2)
        elif( user_1 == 'spock' and user_2 == 'rock' ):
            print("Spock vaporizes rock.")
            print(win_1)

        if( user_1 == 'scissors' and user_2 == 'rock' ):
            print("Rock destroys scissors.")
            print(win_2)
        elif( user_1 == 'scissors' and user_2 == 'rock' ):
            print("Rock destroys scissors.")
            print(win_1)

