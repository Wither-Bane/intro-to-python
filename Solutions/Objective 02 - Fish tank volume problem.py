#Objective 2 - Fish tank volume challenge

length = float(input("Enter the length of the tank in cm:"))
depth = float(input("Enter the depth of the tank in cm:"))
height = float(input("Enter the height of the tank in cm:"))

litres = (length * depth * height) / 1000
gallons = litres * 0.219969

print("The volume of the fishtank is:",litres,"litres.")
print("The volume of the fishtank is:",gallons,"UK gallons.")
