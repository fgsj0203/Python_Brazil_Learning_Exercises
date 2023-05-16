"""
Create code of identify day week
"""


#Variable of input number identify day week
dayWeek = str(input("Enter with number of identify day of week, between 1-7: "))

#Create condition of identify day week
if(dayWeek == 1):
    print("Domingo")
elif(dayWeek == 2):
    print("Segunda")
elif(dayWeek == 3):
    print("Terça")
elif(dayWeek == 4):
    print("Quarta")
elif(dayWeek == 5):
    print("Quinta")
elif(dayWeek == 6):
    print("Sexta")
elif(dayWeek == 7):
    print("Sábado")
else:
    print("Dia inválido")