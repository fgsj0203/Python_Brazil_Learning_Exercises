"""
Calculate salary of employee and discounts
"""

#First variable of received values for calculate salary brute
hoursLabourMonth = int(input("Enter with hours labour in month: "))

#Value of hour labour
valueHourLabour = float(input("Enter with value of labour hour: "))

#Section of operation
salaryBrute = (hoursLabourMonth * valueHourLabour)

#Discount of INSS
discountInss = (salaryBrute * 0.08)

#Discount sindicate
discountSindicate = (salaryBrute * 0.05)

#Discount IR
discountIR = (salaryBrute * 0.11)

#Salary liquid
salaryLiquid = salaryBrute - (discountInss + discountIR + discountSindicate)

"""
Printing values
"""
print("Salary Brute = R$", salaryBrute)
print("INSS = R$", discountInss)
print("IR = R$", discountIR)
print("Sindicate = R$", discountSindicate)
print("Salary Liquid = R$", salaryLiquid)