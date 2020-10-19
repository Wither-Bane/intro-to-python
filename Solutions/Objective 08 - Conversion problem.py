#Objective 8 - Conversion problem

def menu():
    choice = ""
    while choice != "1" and choice != "2" and choice != "3": 
        print("1. cm to inches")
        print("2. inches to cm")
        print("3. Quit")
        choice = input("Enter choice: ")
    return choice

def cm_to_inches():
    #convert cm to inches
    cm = float(input("Enter the number of cm: "))
    inches = cm/2.54
    print(cm,"cm =",inches,"inches")

def inches_to_cm():
    #convert inches to cm
    inches = float(input("Enter the number of inches: "))
    cm = inches*2.54
    print(inches,"inches =",cm,"cm")

#################################################################################
#Main program starts here
choice = menu()    
if choice == "1":
    cm_to_inches()
if choice == "2":
    inches_to_cm()
