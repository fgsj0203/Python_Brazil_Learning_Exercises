"""
Create code print number between zero and ten
"""

#Variable of input number
number = int(input("Enter with number: "))
while(number < 0 or number > 10):
    print("Try again")
    number = int(input("Enter with number: "))

#Printing number final after operation repetition 
print("Number final is: ", number)