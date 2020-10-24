#09-Exceptions.py


### Example 1a

#using the following test table, enter your numbers ...

"""
Test    First number    Second number

1       6               2
2       8               7
3       4               0
4       5               b
"""

#... and observer the output of the following program:

#Run time errors
num1 = float(input("Enter a number to divide: "))
num2 = float(input("Enter a number to divide by: "))
print(num1, "divided by",num2, "is",num1/num2)


#You should have observed the following

"""
Test    First number    Second number   Expected

1       6               2               3.0
2       8               7               1.142
3       4               0               Crash - divide by zero
4       5               b               Crash - invalid character entered
"""

#A program should not crash because it has bad data input.  
#The potential for errors should be considered by the programmer.  


### Example 1b


#Run the following program using the test table of data in "###Example 1a"

#Run time errors
try:
	#Enter two numbers, trapping errors
	num1 = float(input("Enter a number to divide: "))
	num2 = float(input("Enter a number to divide by: "))
	try:
		#Calculate division trapping division by zero
		answer = num1/num2
		print(num1, "divided by",num2, "is",answer)
	except:
		print(num1, "divided by",num2,"is infinity.")
#output error message if a string was entered
except:
	print("Invalid data. Unable to continue.")



#Observer that this code will not crash and a helpful message is displayed!

#There are several types of error that can occur. A summary is given below
"""
TypeError               When an operation is attempted that is invalid for that type of data.

RuntimeError            An error that occurs when the program is running.

NameError               When a name is used that is not known about (often a misspelt variable name).

ZeroDivisionError       Dividing a number by zero.

KeyBoardInterrupt       When a program is interrupted from the keyboard by pressing control+c
"""


#The general pattern for error handling statements is shown below.
"""
try:
    <commands1>
except e:
    <commands2>
else:
    <commands3>
"""
#If <commands1> cause an error, then <commands2> are executed. If <commands1> execute successfully, then <commands3> are executed.

#Note the letter e in the 'except' statement, which you replace with a specific exception to make your code catch multiple exceptions

#below is a modified version of example 1b, with more specific error handling steps


try:
	#Enter two numbers, trapping errors
	num1 = float(input("Enter a number to divide: "))
	num2 = float(input("Enter a number to divide by: "))
	try:
		#Calculate division trapping division by zero
		answer = num1/num2
		print(num1, "divided by",num2, "is",answer)
	except ZeroDivisionError:
		print(num1, "divided by",num2,"is infinity.")
#output error message if a string was entered
except:
	print("Invalid data. Unable to continue.")
