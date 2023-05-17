"""
Calculate sum of average in five numbers
"""

#Initializing variable
sumNumbers = 0

#Operation of calculate sum and average five numbers
for x in range(0,5):
    number = int(input("Enter with number: "))
    sumNumbers = sumNumbers + number #Sum of number


#Operation of calculate average of numbers sum
average = sumNumbers / 5

#Printing final average
print("Average of numbers is: ", average)