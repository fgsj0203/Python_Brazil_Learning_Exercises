"""
Create code of rating concept student in base average notes
"""

#Variables of notes for calculate average
noteOne = float(input("Note one: "))
noteTwo = float(input("Note two: "))

#Calculating average of notes
averageNotes = (noteOne + noteTwo) / 2

#Condition for identify concept of student

if(averageNotes >= 9.0 and averageNotes <= 10.0):
    print("A")
    print("Approved")
elif(averageNotes < 9.0 and averageNotes >= 7.5):
    print("B")
    print("Approved")
elif(averageNotes < 7.5 and averageNotes >= 6.0):
    print("C")
    print("Approved")
elif(averageNotes < 6.0 and averageNotes >= 4.0):
    print("D")
    print("Repproved")
elif(averageNotes < 4.0 and averageNotes >= 0.0):
    print("E")
    print("Repproved")
elif(averageNotes < 0.0 and averageNotes > 10.0):
    print("Invalid")