"""
Create list and average of four notes
"""

#Creating list of notes and average
numberList = []
averageNotes = 0

#Additin numbers in list
for x in range(0,4):
    note = float(input("Enter with a note: "))
    numberList.append(note)
    
#Calculating sum of numbers and average
for x in numberList:
    averageNotes += x

#Printing orders of list numbers
print("Number list is: ",numberList)

#Printing average notes
print("average notes is: ",averageNotes/4)