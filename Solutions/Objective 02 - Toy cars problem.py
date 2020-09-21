#Objective 2 - Toy cars challenge

hourly_rate = 12
car_rate = 0.60

hours_worked = float(input("Enter the number of hours worked:"))
cars_made = int(input("Enter the number of cars made:"))

pay_for_hours = hours_worked * hourly_rate
pay_for_cars = cars_made * car_rate
total_pay = pay_for_hours + pay_for_cars

print("The total pay is:",total_pay)
