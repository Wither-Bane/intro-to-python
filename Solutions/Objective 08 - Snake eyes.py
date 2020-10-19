#Objective 8 - Snake eyes
import random

def roll_dice():
    #Returns the result of rolling the 2 dice
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("Rolled:",dice1,"and",dice2)
    #Snake eyes - lose bank
    if dice1 == 1 and dice2 == 1:
        return "Lose Bank"
    #Single 1 - end turn
    else:
        if dice1 == 1 or dice2 == 1:
            return "Lose"
        else:
            #Points for throw
            return dice1 + dice2

def change_turn(p):
    #Returns the next player's turn
    if p == 1:
        return 2
    else:
        return 1

#################################################################################
#Main program starts here
p1_bank = 0
p2_bank = 0
player_turn = 1

#Play the game until a player wins
while p1_bank < 100 and p2_bank < 100:
    print("-------------------------------------------------------------------")
    print("Player",player_turn,"it's your turn.  Press Enter to roll the dice.")
    input()
    choice = "g"
    running_total = 0
    #Player has a turn until they lose or bank
    while choice == "g":
        throw = roll_dice()
        #Lose bank
        if throw == "Lose Bank":
            print("SNAKE EYES.  You lose your bank")
            if player_turn == 1:
                p1_bank = 0
            else:
                p2_bank = 0
            choice = None
        else:
            #Turn ends when 1 is thrown
            if throw == "Lose":
                print("You rolled a 1 and lost.  Your turn is over.")
                choice = None
                player_turn = change_turn(player_turn)
            else:
                #Add dice to running total
                running_total = running_total + throw
                print("Your total is",running_total)
                choice=""
                #Offer choice to bank or gamble
                while choice != "b" and choice != "g":
                    choice = input("Do you wish to (b)ank or (g)amble: ")
                #Bank total
                if choice == "b":
                    if player_turn == 1:
                        p1_bank = p1_bank + running_total
                        print("You have",p1_bank,"in the bank.")
                    else:
                        p2_bank = p2_bank + running_total
                        print("You have",p2_bank,"in the bank.")
                    player_turn = change_turn(player_turn)
#Output winner
if p1_bank > 100:
    print("Player 1 wins")
else:
    print("Player 2 wins")
            
