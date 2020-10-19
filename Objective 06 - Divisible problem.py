#Objective 5 - Divisible challenge

number1 = int(input("Enter number 1:"))
number2 = int(input("Enter number 2:"))

if number2 == 0:
    print("Error: you cannot divide by 0.")
else:
    remainder = number1 % number2
    if remainder == 0:
        print(number1,"is exactly divisible by",number2)
    else:
        print(number1,"is not exactly divisible by",number2,"there is a remainder of",remainder)
    
