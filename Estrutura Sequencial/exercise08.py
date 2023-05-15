"""
Create code of calculate salary brute of employee in month
"""

#Variable of value hour labour
hourLabourValue = float(input("Please, input of you value of labour hour:"))

#Variable of received hours worked in month
hoursWorkedInMonth = int(input("Hours worked in month: "))

#Operation of calculate salary brute in month
salaryBrute = (hourLabourValue * hoursWorkedInMonth)

#Printing salary brute in month
print("Your salary brute in month is R$ ",salaryBrute)
