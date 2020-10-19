#06-functions.py


###Example1

#Global variables accessed by all subroutines 

MaxNoOfStars=0 

NoOfStars=0 

NoOfSpaces=0 

 

#Set the size of the pyramid of stars 

def InitialiseNoOfSpacesAndStars(): 

    global NoOfSpaces, MaxNoOfStars, NoOfStars 

    MaxNoOfStars=int(input("How many stars at the base (1-40)? ")) 

    #Calculate spaces needed from tip 

    NoOfSpaces = MaxNoOfStars // 2 

    #Set tip of pyramid to one star 

    NoOfStars = 1 

 

#Outputs spaces before stars 

def OutputLeadingSpaces(): 

    global NoOfSpaces 

    for count in range(NoOfSpaces): 

            print(" ",end="") 

 

#Outputs stars 

def OutputLineOfStars(): 

    global NoOfStars 

    for count in range(NoOfStars): 

        print("*",end="") 

    #Move to next line 

    print() 

 

#Adjusts number of stars & spaces after output 

def AdjustNoOfSpacesAndStars(): 

    global NoOfSpaces, NoOfStars 

    NoOfSpaces = NoOfSpaces - 1 

    NoOfStars = NoOfStars + 2 

 

#Main program starts here 

InitialiseNoOfSpacesAndStars() 

while NoOfStars <= MaxNoOfStars: 

    OutputLeadingSpaces() 

    OutputLineOfStars() 

    AdjustNoOfSpacesAndStars() 
    
    
    
    


###Example 2

#Program to output a set of random numbers 

import random 

#Output random numbers 

def outputrandoms(n,m): 

    for counter in range(1,n+1): 

        randomnum = random.randint(1,m) 

        print("Number",counter,"is",randomnum) 

 

#Main program starts here 

number=int(input("How many numbers do you want to output? ")) 

maximum=int(input("What is the maximum number? ")) 

outputrandoms(number, maximum)



### Explanation and comparison of examples 1 and 2

"""
There are two ways to share data between subroutines.  In the first program, the variables were initialised (given a starting value) outside of any subroutine.  That means they are global variables to the program, and their values can be accessed, shared and changed by any subroutine in the program, using the command ‘global’.  

In the second program the variables ‘number’ and ‘max’ are passed into the subroutine outputrandoms.  The values of the variables become n and m in the subroutine outputrandoms.  The variables n and m are different variables to number and max, but the value stored in number and max was passed into n and m.  .  In this example, the variables n and m are lost at the end of the outputrandoms subroutine.  That means they are local variables to the subroutine.
"""




###Example 3

#How functions can be used 

#Returns a positive number from subtraction 

def floor(a, b): 

    f = a - b 

    if f > 0: 

        return f 

    else: 

        return 0 

 

#Main program starts here 

num1=int(input("Enter the first number: ")) 

num2=int(input("Enter the second number: ")) 

print("The floor number is:",floor(num1, num2))


