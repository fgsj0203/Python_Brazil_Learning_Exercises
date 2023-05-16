"""
Code of calculate salary brute and discounts
"""

#Variables of calculate salary brute
hourLabourInMonth = int(input("Enter with hours worked in month: "))
hourValueLabour = float(input("Enter with value of work hour: "))
salaryBrute = (hourLabourInMonth * hourValueLabour)


#Create conditions of calculate discounts and salary final
if(salaryBrute > 0 and salaryBrute <= 900.00):
    print("You salary isent of discounts")
elif(salaryBrute > 900.00 and salaryBrute <= 1500.00):
    discountIR = 0.05                                                   
    valueDiscountIR = (salaryBrute * discountIR)                        
    discountINSS = 0.10                                                  
    valueDiscountINSS = (salaryBrute * discountINSS)
    fgtsValue = 0.11
    salaryLiquid = (salaryBrute - (valueDiscountINSS + valueDiscountIR))
    print("You salary brute is: ", salaryBrute)
    print("Value of discount IR = ", valueDiscountIR)
    print("Value of discount INSS = ", valueDiscountINSS)
    print("Value of addition FGTS = ", (salaryBrute * fgtsValue))
    print("Salary liquid is = ",salaryLiquid)
elif(salaryBrute > 1500.00 and salaryBrute <= 2500.00):
    discountIR = 0.10                                                   
    valueDiscountIR = (salaryBrute * discountIR)                        
    discountINSS = 0.10                                                  
    valueDiscountINSS = (salaryBrute * discountINSS)
    fgtsValue = 0.11
    salaryLiquid = (salaryBrute - (valueDiscountINSS + valueDiscountIR))
    print("You salary brute is: ", salaryBrute)
    print("Value of discount IR = ", valueDiscountIR)
    print("Value of discount INSS = ", valueDiscountINSS)
    print("Value of addition FGTS = ", (salaryBrute * fgtsValue))
    print("Salary liquid is = ",salaryLiquid)
elif(salaryBrute > 2500.00):
    discountIR = 0.20                                                   
    valueDiscountIR = (salaryBrute * discountIR)                        
    discountINSS = 0.10                                                  
    valueDiscountINSS = (salaryBrute * discountINSS)
    fgtsValue = 0.11
    salaryLiquid = (salaryBrute - (valueDiscountINSS + valueDiscountIR))
    print("You salary brute is: ", salaryBrute)
    print("Value of discount IR = ", valueDiscountIR)
    print("Value of discount INSS = ", valueDiscountINSS)
    print("Value of addition FGTS = ", (salaryBrute * fgtsValue))
    print("Salary liquid is = ",salaryLiquid)