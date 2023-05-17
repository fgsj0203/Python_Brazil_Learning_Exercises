"""
Code repetition of received name and password
"""

#Variables for operation repetition
name = str(input("Enter with a name: "))
password = str(input("Enter with a password: "))

#Operation of repetition
while (name == password):
    print("Error, name is equal a password")
    name = str(input("Enter with name: "))
    password = str(input("Enter with password: "))

#Printing values final

print("Name and Password approved!!!!")
print("Name is: ",name)
print("Password final is: ", password)
