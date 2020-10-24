#Objective 10 - RPG attributes

def new_character():
    #Input a new character
    global c_name, c_attack, c_defence
    c_name = input("Enter the character's name: ")
    c_attack = input("Enter the character's attack: ")
    c_defence = input("Enter the character's defence: ")

def save_character():
    #Save the character
    global c_name, c_attack, c_defence
    text_file = open(c_name+".txt", "w")
    text_file.write(c_name+"\n")
    text_file.write(c_attack+"\n")
    text_file.write(c_defence+"\n")
    text_file.close()
    print(c_name,"saved.")

def load_character():
    #Load the character
    global c_name, c_attack, c_defence
    c_name = input("Enter the name of the character to load: ")
    text_file = open(c_name+".txt", "r")
    text_file.readline()
    c_attack = text_file.readline().strip()
    c_defence = text_file.readline().strip()
    text_file.close()
    print(c_name,"Attack:",c_attack,"Defence",c_defence)

#################################################################################
#Main program starts here
c_name = ""
c_attack = ""
c_defence = ""
new_character()
save_character()
load_character()
