#01-if.py


"""
This file teaches
    - The "if-then-else" statement
    - The Boolean type
    - The different comparison operators
    
"""

#"If Statements" allow you to make a choice dependant on almost anything.
#It can be used with text, numbers or users choices.

#The simplest form is shown below:
"""
if <expression>:
    <commands>
"""
#Notice the ":" symbol. This defines the start of a "code block". Everything that follows is indented and ONLY runs if the expression in the IF statement is True
#An example of the IF statement:
colour = input("enter a traffic light colour: ")

if colour == "green":
    print("It is safe for you to cross.")


## ELSE statement

#Usually you'll want something "else" to happen if the IF statement is not True.
#The "else" portion of the IF statement can be used here to handle what happens when the "if" statement is false, as shown below:
"""
if <expression>:
    <commands1>
else:
    <commands2>
"""

#For example, some runnable code might be:

colour = input("enter an invalid traffic light colour: ")

if colour == "green":
    print("It is safe for your to cross.")
else:
    print("STOP! It is not safe to cross.")
    


## ELIF statement

#To make your decision making process more complex, you can introduce additional cases to be considered before the "else" statement is triggered, using the "elif" statement
#The format of the "elif" part of the IF statement is as follows:
"""
if <expressionA>:
    <commands1>
elif <expressionB>:
    <commands2>
elif <expressionC>:
    <commands3>
...

else:
    <finalCommand>
"""

#For example:

colour = input("enter a different traffic light colour (like 'flashing green', instead of 'green'): ")


if colour == "green":
    print("It is safe for your to cross.")
elif colour == "flashing green":
    print("Only cross if you've already started")
else:
    print("STOP! It is not safe to cross.")
    
    
##Boolean-ness
 
#the expressions used in IF statements can evaluate to 'Truthy' or 'Falsey' values. 
#You can determine this by passing the values to the 'bool()' function

#For example, if an expression evalutes to the numbers '0' or '0.0', it's considered Falsey. Any other number is Truthy.
myAge = input("Please enter your age, to the nearest whole number, in years:")
if myAge:
    print("You've been born for a while.")
else:
    print("You could've been born Yesterday!")

#It also applies to Strings: the empty string '' is Falsey, while any other string is Truthy. Prove this to yourself...



##Comparison Operators and Symbols

#When constructing your IF statements, you can compare the parts of your expressions in a variety of ways in Python:

"""
Operator meaning            Operator    Example             Evaluates to
Equal to                    ==          “fred” == “sid”     False
Not equal to                !=          8 != 8              False
Greater than                >           10 > 2              True
Greater than or equal to    >=          5 >= 5              True
Less than                   <           40 < 34             False
Less than or equal to       <=          2 <= 109            True
"""

#You can also compare two or more expressions in combination to form larger expressions using the AND, OR, NOT symbols
#AND    Returns true if both conditions are true.
#OR     Returns true if one of the conditions is true.
#NOT    Reverses the outcome of the expression; true becomes false, false becomes true.

input("\n\nPress enter to exit")
