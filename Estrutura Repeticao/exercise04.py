"""
Create code of biggest population in two countries
"""

#Datas of Country A
countryA = 80000
percentGrowthA = 1.03

#Datas of country B
countryB = 200000
percentGrowthB = 1.015

#Age of calculate time of country A in B
age = 0

#Create operation repetition calculate population of country A and Country B
while(countryA <= countryB):
    countryA = countryA * percentGrowthA
    countryB = countryB * percentGrowthB
    age = age + 1


#Printing data final of countries
print("Country A is population: ", countryA)
print("Country B is population: ", countryB)
print("Time of Country A > Country B: ", age)

