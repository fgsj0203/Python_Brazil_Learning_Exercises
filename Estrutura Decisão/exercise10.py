"""
Create code of calculate salary brute and up money in salary
"""

#Variable of received salary brute
salaryEmployee = float(input("Enter with salary: "))

#Calculating readjustment with about salary
if(salaryEmployee >= 0 and salaryEmployee <= 280.00):
    percentReadjustSalary = 0.20
    newSalary = (salaryEmployee * percentReadjustSalary)
    salaryFinal = (salaryEmployee + newSalary)
    print("Salary brute is: ",salaryEmployee)
    print("You readjustment in salary is 20%")
    print("Value of readjustment is: R$",newSalary)
    print("Salary final is: R$",salaryFinal)
elif(salaryEmployee > 280.00 and salaryEmployee <= 700.00):
    percentReadjustSalary = 0.15
    newSalary = (salaryEmployee * percentReadjustSalary)
    salaryFinal = (salaryEmployee + newSalary)
    print("Salary brute is: ",salaryEmployee)
    print("You readjustment in salary is 15%")
    print("Value of readjustment is: R$",newSalary)
    print("Salary final is: R$",salaryFinal)
elif(salaryEmployee > 700.00 and salaryEmployee <= 1500.00):
    percentReadjustSalary = 0.10
    newSalary = (salaryEmployee * percentReadjustSalary)
    salaryFinal = (salaryEmployee + newSalary)
    print("Salary brute is: ",salaryEmployee)
    print("You readjustment in salary is 10%")
    print("Value of readjustment is: R$",newSalary)
    print("Salary final is: R$",salaryFinal)
elif(salaryEmployee > 1500.00):
    percentReadjustSalary = 0.05
    newSalary = (salaryEmployee * percentReadjustSalary)
    salaryFinal = (salaryEmployee + newSalary)
    print("Salary brute is: ",salaryEmployee)
    print("You readjustment in salary is 5%")
    print("Value of readjustment is: R$",newSalary)
    print("Salary final is: R$",salaryFinal)