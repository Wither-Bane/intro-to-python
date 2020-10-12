#Objective 4 - Nitrate challenge

nitrate = float(input("Enter the nitrate level: a number between 1 and 50:"))

if nitrate > 10:
    print("Dose 3ml")
elif nitrate > 2.5:
    print("Dose 2ml")
elif nitrate >1:
    print("Dose 1ml")
else:
    print("Dose 0.5ml")
    
