"""
Code of create weight ideal for Man and Women
"""

#Variable of received height of people
height = float(input("Please, input you height: "))

#Operation for calculate weight ideal for Man and Women
weightMan = (72.7 * height) - 58
weightWomen = (62.1 * height) - 44.7

#Printing values of weight peoples
print("Weight man is: ", weightMan)
print("Weight Women is: ", weightWomen)