#Objective 2 - Circle properties challenge

diameter = float(input("Enter the diameter of the circle in cm:"))
arc_angle = float(input("Enter the arc angle:"))

radius = diameter / 2
circumference = 3.14 * diameter
arc_length = (circumference * arc_angle) / 360

print("The radius is",radius,"cm")
print("The area is",3.14 * (radius * radius),"cm2")
print("The circumference of the circle is",circumference)
print("The arc length of the circle is",arc_length)
