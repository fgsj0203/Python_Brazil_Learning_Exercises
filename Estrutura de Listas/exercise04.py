"""
Create code of reading character and identify consonant and vogal
"""

#Creating list empty of received characteres
characterList = []

#Creating list of vogal
listVogal = []

#Creating list of consonant
consonantList = []

#Operation of received data and identify if vogal or consonant
for x in range(0,10):
    letter = str(input("Enter with character: "))
    characterList.append(letter) #additing character general
    if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        listVogal.append(letter)
    else:
        consonantList.append(letter) 

#Printing list of characters original
print("List original of character is: ",characterList)

#Printing list of character vogal
print("List of vogals is: ", listVogal)

#Printing list of character consonant
print("List of consonants is: ",consonantList)