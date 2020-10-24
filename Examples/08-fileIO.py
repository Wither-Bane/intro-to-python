#08-fileIO.py

### Example 1

#Guess what the following program does:

#Open a text file for writing
text_file = open("data.txt", "w")
text_file.write("This is a simple way to save data\n")
text_file.write("one line at a time")
text_file.close()
print("File created.")


#You should find a new file called data.txt in the same folder that you saved the program in.  Open it and examine the contents.
#Note the "w" in line 2.  This means write data to the file.
#Note the \n in line 3.  This is known as an escape sequence and adds a carriage return to start a new line.



### Example 2

#Can you infer what happens with this program:

#Open a text file for reading
text_file = open("data.txt", "r")
print(text_file.read())
text_file.close()


# Change the program so that 3 lines of text are written to a file and then read it back in again.


### Example 3

#It is often useful to read in all the data from a file line by line until you reach the end of the file. 
#To do this we would want to combine an iteration with a file read:

#Open a text file for reading
text_file = open("data.txt", "r")

#Read each line into a variable and output
while True:
    a = text_file.readline()
    if not a: 
        break
    print(a)
text_file.close()

#Note how we can use an infinite loop and a break command to read all the lines in the file until no more lines are found.


### Example 4

#Each line in the text file has a hidden \n new line escape sequence to indicate the next item of data is on a new line.  
#This has to be removed before selection statements can be used because C is not the same as C\n.

#The method .strip will remove the escape sequence from the string. E.g. :

#Open a text file for reading
text_file = open("data.txt", "r")

x = text_file.readline()
x = answer.strip()


### Example 5

#As you have seen above, If you assign the file object to a variable, you can explicitly close it using .close()

f = open('data.txt','r')
buf = f.readlines()
f.close()

#Alternatively (and more generally preferred), you can use the with keyword (Python 2.5 and greater): 
with open('test.txt','r') as f:
    buf = f.readlines()

#you can check this by using the ".closed" property of variables that store file objects.
print("Is file f closed? the answer is", f.closed)