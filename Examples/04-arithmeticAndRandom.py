#04-arithmeticAndRandom.py

#Get user input 

number1=int(input("Enter first number: ")) 

number2=int(input("Enter second number: ")) 

 

#Make calculations 

power_of_result = number1 ** number2 

division_result = number1 / number2 

integer_division_result = number1 // number2 

modulus_result = number1 % number2 

 

#Output results 

print() 

print(number1,"to the power of",number2,"is",power_of_result) 

print(number1,"divided by",number2,"is",division_result) 

print(number1,"divided by",number2,"is",integer_division_result) 

print(number1,"divided by",number2,"has a remainder of",modulus_result)



### Random Module

import random

#Roll the dice 

random_number = random.randint(1,6) 

print("You rolled a",random_number) 




### Math Module

import math

#Display everybody's famous constant
print("the approximate value of Pi stored in python ==> ", math.pi)

#Displays the first argument raised to the power of the second argument
ans = math.pow(2,3)
print("2 to the power of 3 = ", ans)

#Displays the square root of a number
ansRooted = math.sqrt(ans)
print("The root of 8, our previous answer, is", ansRooted)
