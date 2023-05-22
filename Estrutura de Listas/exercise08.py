"""
Create code of vector with 10 elements and calculate a value potential of two
"""

#Creating list empty
numbers_list = []

numbers_list_potential_two = []

#Creating operation of addition numbers in list
for x in range(0,10):
    number = int(input("Enter with a number: "))
    numbers_list.append(number)

#Calculating elements numbers of potential two
for x in (numbers_list):
    numbers_list_potential_two.append(x ** 2) #Using point "x" of function for iteration calculate potential in elements of list previous


#Printing list final with elements multiplicate potential two
print("List final of elements with a potential two: ",numbers_list_potential_two)
