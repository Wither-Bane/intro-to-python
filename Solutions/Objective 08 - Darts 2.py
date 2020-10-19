#Objective 8 - Darts

def new_game():
    global score
    score = 501
    print("New game.  Player starts at 501 points.")

def input_darts():
    global score
    dart1 = int(input("Dart 1:"))
    if score - dart1 < 2:
        print("Bust")
        return -1
    else:
        dart2 = int(input("Dart 2:"))
        if score - dart2 - dart1 < 2:
            print("Bust")
            return -1
        else:
            dart3 = int(input("Dart 3:"))
            if score - dart3 - dart2 - dart1 < 2:
                print("Bust")
                return -1
            else:
                return dart1 + dart2 + dart3

def play_game():
    global score
    while score != 0:
        darts = input_darts()
        if darts > -1:
            print(darts,"scored.")
            score = score - darts
            print("Score:",score)
        if score == 0:
            print("Player 1 wins the game")

#################################################################################
#Main program starts here
new_game()
play_game()
