"""
Create code of identifies gender of people
"""

#Variable of received gender of people
genderPeople = str(input("Enter with gender people, female -> f or Male -> m : "))

#Operation of converted letter for small size
genderSmallLetter = (genderPeople.lower())

#Printing letter in small size
print(genderSmallLetter)

#Create condition for identify gender of people
if(genderSmallLetter == "f"):   #input data of variable is "F" of Female
    print("You Female")
else:
    print("You Male")           #If not input "F" this is Male "M"