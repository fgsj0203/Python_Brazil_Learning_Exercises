"""
Create list with 20 numbers and calculate numbers pair and odd
"""

#Creating list empty
listNumbersGeneral = []

#Creating list of numbers pair
listNumbersPair = []

#Creating list of numbers odd
listNumbersOdd = []

#Operation of calculating numbers pair and odd
for x in range(0,20):
    number = int(input("Enter with a number: "))
    listNumbersGeneral.append(number)
    if (number % 2 == 0):
        listNumbersPair.append(number)
    else:
        listNumbersOdd.append(number)


#Printing list of values
print("List original is: ",listNumbersGeneral)
print("List of numbers pair: ",listNumbersPair)
print("List of numbers odd: ",listNumbersOdd)
