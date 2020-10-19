#Objective 3 - Name separator challenge

full_name = input("Enter your full name:")

space = full_name.find(" ")
forename_characters = full_name[:space]
surname = len(full_name) - space - 1
surname_characters = full_name[-surname:]

print("Forename:",forename_characters)
print("Surname:",surname_characters)
