"""
Create code of calculate weight ideal of people using you height
"""

#Variable of received height
heightPeople = float(input("Please, you input height: "))

#Operation of calculate weight ideal
weightIdeal = (72.7 * heightPeople) - 58

#Printing weight ideal
print("You weight ideal is: ", weightIdeal, "KG")