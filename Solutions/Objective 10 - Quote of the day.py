#Objective 10 - Quote of the day

def quote():
    import random
    quotes = []
    counter = 0
    text_file = open("Objective 10 - Quote of the day quotes.txt", "r")

    while True:
        quote = text_file.readline().strip()
        if not quote: break
        quotes.append(quote)
        counter = counter + 1
    text_file.close()

    n = random.randint(0,counter)
    return quotes[n]

#################################################################################
#Main program starts here
print(quote())
