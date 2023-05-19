"""
Create list of ten numbers and printing in order inverse
"""

#Creating lists empty
listNumbers = []

#Operation of additing numbers in list
for x in range(0,10):
    number = int(input("Enter with number: "))
    listNumbers.append(number)

#Printing numbers in order original
print("List of order original numbers: ", listNumbers)

#Printing list of numbers in order inverse using function "inverse"
listNumbers.reverse()
print("List of order inverse numbers: ",listNumbers)
