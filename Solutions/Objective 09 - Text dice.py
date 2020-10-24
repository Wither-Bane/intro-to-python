#Objective 9 - Text dice problem

import random

def dice():
    dice_face = ["one","two","three","four","five","six"]
    return dice_face[random.randint(0,5)]

#################################################################################
#Main program starts here
print(dice())
