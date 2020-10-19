#Objective 5 - Cash machine challenge

balance = 231

print("Balance £",balance)
withdraw = int(input("Enter how much do you wish to withdraw:"))

if balance - withdraw < 0:
    print("You cannot go over-drawn.")
else:
    if withdraw % 20 == 0 and withdraw % 10 == 0:
        balance = balance - withdraw
        print("New balance:",balance)
    else:
        print("The machine can only dispense £20 and £10 notes.")
        
