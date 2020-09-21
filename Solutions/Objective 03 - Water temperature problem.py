#Objective 4 - Water temperature challenge

temperature = float(input("Enter the temperature:"))

if temperature >= 100:
    print("The water is boiling.")
elif temperature <= 0:
    print("The water is frozen")
else:
    print("The water is neither boiling or frozen.")
