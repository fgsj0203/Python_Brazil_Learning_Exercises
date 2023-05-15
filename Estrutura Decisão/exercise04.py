"""
Create code of identify vogal or consonant
"""

#Variable of received data is letter
letter = str(input("Enter with letter: "))

#Operation of converted letter for small size
converterLetterSmall = letter.lower()

if ((converterLetterSmall != "a") and (converterLetterSmall != "e") and (converterLetterSmall != "i") and (converterLetterSmall != "o") and (converterLetterSmall != "u")):
    print("You letter is consonant, a letter is: ",converterLetterSmall)
else:
    print("You letter is vogal, a letter is: ", converterLetterSmall)