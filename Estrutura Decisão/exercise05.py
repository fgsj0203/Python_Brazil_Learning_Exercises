"""
Create code for printing situation school and calculating average notes
"""

#Variables of received notes
noteOne = float(input("Enter with note One: "))
noteTwo = float(input("Enter with note Second: "))

#Operation of calculate average notes
averageNotes = (noteOne + noteTwo) / 2 

#Printing note average
print("You average is: ", averageNotes)

#Conditions of situation school
if(averageNotes > 10.0):
    print("Average invalid")
elif (averageNotes == 10.0):
    print("Approved with distinction")
elif (averageNotes < 10.0 and averageNotes >= 7.0):
    print("Approved")
elif (averageNotes < 7.0 and averageNotes >= 0.0):
    print("disapproved")
elif (averageNotes < 0.0):
    print("average invalid")
    