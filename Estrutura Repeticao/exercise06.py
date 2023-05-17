"""
Printing five numbers and calculate bigger number
"""

#Variable of received bigger number
biggerNumber = 0

#Operation for calculate bigger of five numbers
for x in range(0,5):
    number = int(input("Enter with a number: "))
    if number > biggerNumber:
        biggerNumber = number


#Printing bigger number final
print("Bigger number is: ",biggerNumber)


