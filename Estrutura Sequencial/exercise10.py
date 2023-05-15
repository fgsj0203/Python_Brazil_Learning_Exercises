"""
Converter temperature of Celsius -> Farenheit
"""

#First variable of received temperature in Celsius
temperatureCelsius = int(input("Please, input temperature in C°: "))

#Operation of converter temperature Celsius for Farenheit
converterTemperature = (temperatureCelsius * 1.8) + 32

#Printing temperature converted
print("Temperature in C° -> F° is: ", converterTemperature,"F°")