#05-strManipulationAndStrFunctions.py



##Working with strings 
forename=input("Enter your surname: ") 
forename_uppercase=forename.upper() 
print("Your name in capital letters is:",forename_uppercase) 

forename_lowercase = forename.lower()
print("Your name in lowercase letters is:",forename_lowercase)






##Slicing

#[:?] returns a number of characters to the left of a string 
sentence = "I saw a wolf in the forest. A lonely wolf." 
print("the sentence is '"+sentence+"'")
characters = sentence[:5] 
print(characters)

#to output the last 12 characters in the sentence instead of the first 5, use [-12:] instead of [:5]
characters = sentence[-12:] 
print(characters)


#[start:end]. the code below returns a number of characters in the middle of a string 
sentence = "I saw a wolf in the forest. A lonely wolf." 
characters = sentence[20:26] 
print(characters)



##String functions

# "len()" returns the number of characters in a string 
surname = input("Enter your surname: ") 
length_name = len(surname) 
print("There are",length_name,"letters in your name.") 

#find returns the location of one string inside another 
sentence = "I saw a wolf in the forest. A lonely wolf." 
print(sentence) 
word = input("Enter the word to find: ") 
position = sentence.find(word) 
print("The word",word,"is at character",position) 


# "str()" returns the string representation of the argument.
print("55 + 6 = " str(55+6))