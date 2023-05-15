"""
Code of print bigger in three numbers
"""

#Variables of received numbers
numberOne = int(input("Enter with number one: "))
numberTwo = int(input("Enter with number two: "))
numberThree = int(input("Enter with number three: "))

if ((numberOne > numberTwo) and (numberOne > numberThree)):
    print("Bigger is one number: ", numberOne)
elif((numberTwo > numberThree) and (numberTwo > numberOne)):
    print("Bigger is number two: ", numberTwo)
elif((numberThree > numberOne) and (numberThree > numberTwo)):
    print("Bigger is number three: ", numberThree)