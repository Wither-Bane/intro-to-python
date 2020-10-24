#Objective 9 - Currency converter problem

def exchange(country,gpb):
    rates = ["USD",1.26,"Euro",1.11,"Rupee",90.45,"Yen",143]
    index = 0
    #Find the currency in the list/array
    while rates[index] != country:
        index = index + 1
    if rates[index] == country:
        #Currency found
        return round(rates[index+1]*gbp,2)
    else:
        #Currency not found
        return None

#################################################################################
#Main program starts here
gbp = float(input("Enter the number of British Pounds: "))
country = input("Enter the currency: ")
value = exchange(country,gbp)
if value != None:
    print(value)
else:
    print("Currency not found.")
