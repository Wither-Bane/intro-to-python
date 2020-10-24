#Objective 9 - Notebook problem

notebook = []

def initialise_notebook():
    global notebook
    for counter in range(0,10):
        notebook.append("")

def output_notebook():
    global notebook
    for counter in range(0,10):
        print(counter,":",notebook[counter])
        
def change_note():
    global notebook
    note = int(input("Enter the number of the note to change: "))
    text = input("Enter the note: ")
    notebook[note] = text

#################################################################################
#Main program starts here
initialise_notebook()
while True:
    output_notebook()
    change_note()
