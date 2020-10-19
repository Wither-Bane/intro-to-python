#Objective 8 - Darts (simple)

score = 501
print("New game. Player starts at 501 points.")
while score != 0:
    darts = int(input("Enter the total of 3 darts: "))
    if score - darts > 1:
        score = score - darts
        print("Score:",score)
    else:
        if score - darts == 0:
            score = score - darts
            print("Player 1 wins the game")
