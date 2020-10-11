#00-intro.py

"""
This file teaches:
	-What a variable is
	-What data types are
	-basic user input (Objective 1) and output (Objective 2)
	
"""



##Variables and DataTypes
"""

#Assigns a value to a variable
variableName = <value> 
"""
#For example:
myString = "hello world"
myNumber = 89
myOtherNumber = 3.14
myBoolean = True

#But what are these different values above?
#These are examples of the DataTypes you can use in Python
#There are four data types you need to know about:

#1. Integers, known as 'int' in Python, are whole numbers. for example:
myInteger = 45

#2. Strings, known as 'str' in Python, are sequences of characters that can include letters, spaces and other characters. For example:
myString = "qwerty123" #Notice the surronding quote marks. Single or double quotes can be used

#3. Floats, known as 'float' in Python, are numbers with a fractional part. Also known as a real (or decimal) number. For example:
myFloat

#4. Boolean values, known as 'bool' in Python, are Boolean or logical data that can only have one of two values: True or False. For example:
am_i_hungry = True




##Basic input and output (aka I/O)


##Objective 1

#You can output information to the screen through the use of the built-in function 'print()', as shown below:

print("Hello world")

#There will also be times in your programs when you want to capture information from the user. You can do this using another built-in function: input(). This function prompts for input from the user, and the data that is entered can be assigned to a variable for later usage, as shown below (as per the interactive interpreter):

"""
>>> reply=input("Enter your name: ")
Enter your name: Fred
>>> reply
'Fred'
"""
#Exercises: see #Objective-01.py for tasks
#Solutions: see "Objective 01 - ASCII art problem.py" and "Objective 01 - Visual dice problem.py" for solutions



##Objective 2

#If you need to use the input recieved as something other than a string, you can use several built-in functions to convert the string returned by 'input()':

#   -'int()' converts a string (or float) value into an integer number. For example, the following converts the input recieved into an integer and stores that integer in the number variable:
number_int = int(input("Please enter the number of T-shirts you require:"))
print(number) # this will print the number you entered at the prompt


#   -similarly, 'float()' Converts a string or integer into a float and 'str()' converts a number into a string. 
#For example:
number_float = float(input("please enter Pi to 2 decimal places: "))
print(number_float)

#Exercises: see #Objective-02.py for tasks
#Solutions: see relevant .py files for relevant solutions


input("\n\nPress enter to exit")