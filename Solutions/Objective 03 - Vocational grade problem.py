#Objective 4 - Vocational grade challenge

mark = int(input("Enter the mark:"))

if mark < 40:
    print("FAIL")
elif mark >= 40 and mark < 60:
    print("PASS")
elif mark >= 60 and mark < 80:
    print("MERIT")
else:
    print("DISTINCTION")
