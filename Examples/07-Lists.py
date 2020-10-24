#07-Lists.py

### Example 1

#Sentence (the variable below) is an example of a list, or one dimension array: a group of elements with the same name and data type.
#NOTE: In python, the first element in the list has an index number of ZERO (not number 1 for the 1st element)!

#Declare list and data set
sentence = ["The","quick","grey","fox","jumps"]
#Output contents of list
print(sentence[0])
print(sentence[1])
print(sentence[2])
print(sentence[3])
print(sentence[4])



#the list currently looks like this (see output of below command)
print(sentence)


#Now, Try and enter the colour brown and see what happens to the list
sentence[2] = input("Enter new colour: ")
print(sentence)

#Note how it is possible to change an individual element of an array by referring to the index.



### Example 2

# You don’t always want to populate the array with data when it is declared.  
# For example, to declare an array of 100 elements, you would use the alternative syntax:

item = []
for counter in range(100):
	item.append(0)

#You can then put data into the array using the syntax:

        item[0] = "Alpha"
        item[99] = "Omega"

#Note, again, that indexes always start at zero.  So, one hundred elements is 0-99.


### Example 3

#The power of lists often comes by combining them with iterations.
#Enter this code as an alternative to the first program and notice how the amount of code is much reduced ...
# ... when you use a for loop to output each of the indexes of the list.

sentence = ["The","quick","brown","fox","jumps"]
for index in range(0,4):
	print(sentence[index])



### Example 4

#Try entering this program and test by entering 8743 when prompted for a product code:
#Note how an iteration and Boolean variable can be used to go through all the indexes of an array to find an item.
#(This is not the best way to write this program, but does illustrate how a number of programming concepts can be combined)


#Declare array and set data
product = ["1262", "Cornflakes", "£1.40", "8743", "Weetabix", "£1.20", "9512", "Rice Krispies", "£1.32"]
product_code=0  #Product code to find
found=False     #Whether product was found in array
        
#Ask use for the product code to find
product_code=input("Enter the product to find: ")

#Use a loop to cycle through the indexes
counter = 0
found = False
while found == False and counter != 9:
    #Output the product if found
    if product[counter] == product_code:
        print(product[counter + 1])
        print(product[counter + 2])
        found = True
    counter = counter + 1
    
#Output message if product is not found
if counter == 9:
    print("Product not found")



### Example 5

#Have a look at the following program and try to guess what happens
#Afterwards, modify it in the following ways:
#   -Change the program so that a ‘pick axe’ is added to the inventory
#   -Change the program so the inventory is output and the user can choose which item to drop.

#Create a new list
inventory = []
#Add items to the list
inventory.append("torch")
inventory.append("gold coin")
inventory.append("key")

#Remove items from the list
inventory.remove("gold coin")

#Sort the items into alphabetical order
inventory.sort()

#Output all the items in the list
for counter in range (len(inventory)):
    print(inventory[counter])


