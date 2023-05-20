"""
Create code of calculate notes and average studentes
"""

#Creating list empty for storage notes and average
averageStudent = []
averageStudenAproved = []

#Initializing variable of sum notes
sumNotes = 0

#Operation for calculate notes and average of students
for x in range(0,2):
        noteOne = float(input("Enter with a first note: "))
        noteTwo = float(input("Enter with a second note: "))
        noteThree = float(input("Enter with a third note: "))
        noteFour = float(input("Enter with a Fourth note: "))
        sumNotes = (noteOne + noteTwo + noteThree + noteFour)
        averageNote = (sumNotes/4)
        if(averageNote >= 7.0 and averageNote <= 10.0):
            averageStudenAproved.append(averageNote)
            


#Printing values of list with student aproved
print("Student aproved: ",averageStudenAproved)

#In development
