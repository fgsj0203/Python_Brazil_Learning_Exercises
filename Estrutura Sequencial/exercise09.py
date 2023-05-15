"""
Create code of converter temperature farenheit for Celsius
"""

#Create variable of received temperature in farenheit
temperatureFarenheit = float(input("Please, input temperature in farenheite: "))

#Formule of converter Farenheit -> Celsius
temperatureCelsius = 5 * ((temperatureFarenheit-32) / 9)

#Printing temperature calculate
print("Temperature of Farenheite -> Celsius is: ", temperatureCelsius, "C°")