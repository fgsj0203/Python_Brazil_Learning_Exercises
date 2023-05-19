"""
Create code of received numbers pair and odd
"""

#Operation of calculate numbers pair and odd
for x in range(0,10):
    number = int(input("Enter with number: "))
    if (number % 2 == 0):
        print("Number is pair", number)
    else:
        print("Number is odd: ", number)

