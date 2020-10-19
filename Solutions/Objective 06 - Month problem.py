#Objective 5 - Month challenge

year = int(input("Enter the year:"))
month = int(input("Enter the month:"))

if month == 1:
    print("January has 31 days")
if month == 2:
    if year % 4 == 0:
        print("February has 29 days")
    else:
        print("February has 28 days")
if month == 3:
    print("March has 31 days")
if month == 4:
    print("April has 30 days")
if month == 5:
    print("May has 31 days")
if month == 6:
    print("June has 30 days")
if month == 7:
    print("July has 31 days")
if month == 8:
    print("August has 31 days")
if month == 9:
    print("September has 30 days")
if month == 10:
    print("October has 31 days")
if month == 11:
    print("November has 30 days")
if month == 12:
    print("December has 31 days")
