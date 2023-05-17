"""
Create code of validation inputs data personal
"""

#Variables data inputs personal
#Validation of size name
name = str(input("Enter with name: "))
sizeName = len(name)
while(sizeName <= 3):
    print("Size name invalid, need most three characteres")
    name = str(input("Enter with a name: "))
    sizeName = len(name)

#Validation of interval age
age = int(input("Enter with age: "))
while(age < 0 or age > 150):
    print("Age invalid, try again")
    age = int(input("Enter again you age: "))

#Validation of salary
salary = float(input("Enter with salary: "))
while(salary < 0):
    print("Salary invalid, try again")
    salary = float(input("Enter with salary: "))

#Validation of gender people
genderPeople = str(input("Enter with gender, male or female: "))
smallSizeLetter = genderPeople.lower()
while(smallSizeLetter != "f" and smallSizeLetter != "m"):
    genderPeople = str(input("Enter with gender, male or female again: "))
    smallSizeLetter = genderPeople.lower()

#Validation of state civil
stateCivil = str(input("Enter with you state civil: "))
smallSizeConverterLetter = stateCivil.lower()
while (smallSizeConverterLetter != "s" and smallSizeConverterLetter != "c" and smallSizeConverterLetter != "v" and smallSizeConverterLetter != "d"):
    print("State civil invalid, try again")
    stateCivil = str(input("Enter with you state civil: "))
    smallSizeConverterLetter = stateCivil.lower()


print("********** Register final **********")
#Printing final of data inputed
print("Name is: ",name)
print("Age is: ", age)
print("Salary is: ",salary)
print("Gender people: ",genderPeople)
print("state civil is: ",stateCivil)