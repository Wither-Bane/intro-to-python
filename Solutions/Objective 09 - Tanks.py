#Objective 9 - Tanks
import random

def output_board(player):
    global board, board_size
    #Output a graphical representation of the board
    print(" ",end="")
    for x in range(board_size):
        print(x,end="")
    print()
    for y in range(board_size):
        print(y,end="")
        for x in range(board_size):
            print (board[player][x][y],end="")
        print()

def place_tanks(player,num_tanks):
    #Place 10 tanks for the player
    global board, board_size
    print("Player",player+1,"place your tanks.")
    choice = input("Do you want the computer to place random tanks for you? y/n: ")
    for tank in range(1,num_tanks+1):
        print("Place tank",tank)
        valid = False
        #Input valid board position
        while not valid:
            if choice == "y":
                x = random.randint(0,board_size-1)
                y = random.randint(0,board_size-1)
            else:
                x = int(input("Enter the x position: "))
                y = int(input("Enter the y position: "))     
            if board[player][x][y] == "-":
                #Put a tank on the board.  Tanks are stored with a T
                board[player][x][y] = "T"
                valid = True
            else:
                print("You already have a tank placed there.")
        output_board(player)
    #Clear screen
    for line in range(50):
        print()
    print("All tanks placed.")
    
def fire(player):
    #Handles shooting
    global board
    if player == 0:
        opponent = 1
    else:
        opponent = 0
    x = int(input("Enter the x position: "))
    y = int(input("Enter the y position: "))
    if board[opponent][x][y] == "T":
        print("Hit")
        #Hit tanks are stored with an X
        board[opponent][x][y] = "X"
        return "Hit"
    else:
        print("Miss")
        return "Miss"
   
def play_game():
    global num_tanks
    #Plays the game
    player = 0
    #Play until all the tanks are shot
    while score[0] < num_tanks and score[1] < num_tanks:
        print("Player",player+1,"it's your turn.")
        #Fire at opponent
        result = fire(player)
        if result == "Hit":
            score[player] = score[player] + 1
        #Next player
        if player == 0:
            player = 1
        else:
            player = 0
    #Announce winner
    print("---------- WINNER ----------")
    if player == 1:
        print("Player 1 wins")
    else:
        print("Player 2 wins")

#################################################################################
#Main program starts here
#Setup board
num_tanks = 10 #Constant for the number of tanks
board_size = 8 #Constant for the size of the board
board = [[["-" for y in range(board_size)] for x in range(board_size)] for player in range(2)]
print(board)
#Setup score
score = []
score.append(0)
score.append(0)
#Place player tanks
place_tanks(0,num_tanks)
place_tanks(1,num_tanks)
#Play the game
play_game()

