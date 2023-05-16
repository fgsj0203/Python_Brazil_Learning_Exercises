"""
Code of input three numbers and printing in descending order
"""

#Variables numbers
numberOne = int(input("Enter number one: "))
numberTwo = int(input("Enter number two: "))
numberThree = int(input("Enter number three: "))


#Operation of decision and printing in descending order
if ((numberOne > numberTwo) and (numberOne > numberThree) and (numberTwo > numberThree)):
    print("Printing order descending number")
    print(numberOne)
    print(numberTwo)
    print(numberThree)
elif((numberOne > numberTwo) and (numberOne > numberThree) and (numberThree > numberTwo)):
    print("Printing order descending number")
    print(numberOne)
    print(numberThree)
    print(numberTwo)
elif((numberTwo > numberThree) and (numberTwo > numberOne) and (numberThree > numberOne)):
    print("Printing order descending number")
    print(numberTwo)
    print(numberThree)
    print(numberOne)
elif((numberTwo > numberThree) and (numberTwo > numberOne) and (numberOne > numberThree)):
    print("Printing order descending number")
    print(numberTwo)
    print(numberOne)
    print(numberThree)
elif((numberThree > numberOne) and (numberThree > numberTwo) and (numberOne > numberTwo)):
    print("Printing order descending number")
    print(numberThree)
    print(numberOne)
    print(numberTwo)
elif((numberThree > numberOne) and (numberThree > numberTwo) and (numberTwo > numberOne)):
    print("Printing order descending number")
    print(numberThree)
    print(numberTwo)
    print(numberOne)