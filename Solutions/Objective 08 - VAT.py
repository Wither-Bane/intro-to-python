#Objective 8 - VAT

def vat(price):
    return price*0.2

price = float(input("Enter the price £"))
total = price + vat(price)
print("Total £","{:.2f}".format(total))
