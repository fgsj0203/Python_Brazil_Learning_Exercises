"""
Create code of identify day shift
"""

#Create variable of received shift day
shiftDay = str(input("Enter with shift day: "))

#Operation for converter letter for small size and identify shift day
smallLetterShiftDay = shiftDay.lower()

#Create conditions of identify shift day
if (smallLetterShiftDay == "m"):
    print("Bom dia")
elif (smallLetterShiftDay == "v"):
    print("Boa tarde")
elif (smallLetterShiftDay == "n"):
    print("Boa noite")
else:
    print("Turno inválido")