#03-WhileLoops.py


##Intro

#'While' loops are another method of iteration, which runs based on a condition (as opposed to count-controlled for loops)

#The format of a while loop is:

"""
while <condition>:
    <commands>
"""
#'While' loops execute <commands> whilst <condition> is true. That is, While loops are pre-condition controlled loops

#For example:

answer = "N"
counter=0 

while answer != "Y":
    print("Are you hungry? You have been asked ",counter," times")
    answer = input("Please respond Y or N: ")
    counter = counter + 1
    print("Please get something to eat!")
    
    
##NOTES:

#It is possible to create 'infinite' while loops, where the condition is always true and runs forever!
#This may be useful in some cases, but may also be a mistake in others.

#For example

while True:
    print(" I love CANDY!!!")
    
    
#To be able to use these loops, one usually includes a 'break' statement to allow for the exiting of the loop, as shown below:

while True:

    if count = 5:
        print(" I love CANDY!!!")
    else:
        print("i'm bored of candy now")
        break