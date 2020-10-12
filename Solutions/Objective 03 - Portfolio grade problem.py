#Objective 4 - Portfolio grade challenge

analysis = int(input("Enter the analysis mark:"))
design = int(input("Enter the design mark:"))
implementation = int(input("Enter the implementation mark:"))
evaluation = int(input("Enter the evaluation mark:"))

total = analysis + design + implementation + evaluation

if total < 2:
    print("Grade: U")
    print("You needed",2 - total,"more marks to get to the next mark band.")

if total >= 2 and total < 4:
    print("Grade: 1")
    print("You needed",4 - total,"more marks to get to the next mark band.")

if total >= 4 and total < 13:
    print("Grade: 2")
    print("You needed",13 - total,"more marks to get to the next mark band.")

if total >= 13 and total < 22:
    print("Grade: 3")
    print("You needed",22 - total,"more marks to get to the next mark band.")

if total >= 22 and total < 31:
    print("Grade: 4")
    print("You needed",31 - total,"more marks to get to the next mark band.")

if total >= 31 and total < 41:
    print("Grade: 5")
    print("You needed",41 - total,"more marks to get to the next mark band.")

if total >= 41 and total < 54:
    print("Grade: 6")
    print("You needed",41 - total,"more marks to get to the next mark band.")

if total >= 54 and total < 67:
    print("Grade: 7")
    print("You needed",67 - total,"more marks to get to the next mark band.")

if total >= 67 and total < 80:
    print("Grade: 8")
    print("You needed",80 - total,"more marks to get to the next mark band.")

if total >= 80:
    print("Grade: 9")
