"""
Create code of print bigger number and smaller number
"""

#three Variables of received numbers
numberOne = int(input("Enter with number one: "))
numberTwo = int(input("Enter with number two: "))
numberThree = int(input("Enter with number three: "))
 
#Condition of calculate bigger and smaller number
if ((numberOne > numberTwo) and (numberOne > numberThree) and (numberTwo > numberThree)):
    print("Bigger number is: ",numberOne)
    print("Smaller number is: ", numberThree)
elif((numberTwo > numberThree) and (numberTwo > numberOne) and (numberThree > numberOne)):
    print("Bigger number is: ",numberTwo)
    print("Smaller number is: ",numberOne)
elif((numberThree > numberOne) and (numberThree > numberTwo) and (numberOne > numberTwo)):
    print("Bigger number is: ",numberThree)
    print("smaller number is: ",numberTwo)



#Printing bigger and smaller values using function native of Python 
print(max(numberOne, numberTwo, numberThree))
print(min(numberOne, numberTwo, numberThree))