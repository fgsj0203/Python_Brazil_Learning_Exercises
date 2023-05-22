"""
Create three lists for addition elements and list final with all elements of two lists 10 elements 
"""

#Creating lists 
numbers_list_a = []
numbers_list_b = []
numbers_list_final = []

#Creating operation of addition elements in lists
for x in range(0,10):
    number = int(input("Enter with a number: "))
    numbers_list_a.append(number)
    number = int(input("Enter with second number: "))
    numbers_list_b.append(number)

#Printing lists previous
print("List A of numbers: ", numbers_list_a)
print("List B of numbers: ", numbers_list_b)

#Printing list final
print("List final is: ",numbers_list_a + numbers_list_b)
