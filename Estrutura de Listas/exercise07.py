"""
Create code of input weight and hight of peoples and printing in order reverse
"""

#Creating lists empty
#List of hight people
list_people_hight = []

#List of weight people
list_people_weight = []


#Operation of calculating and received datas of weight and hight
for x in range(0,5):
    weight_people = int(input("Enter with weight: "))
    list_people_weight.append(weight_people)
    hight_people = float(input("Enter with hight: "))
    list_people_hight.append(hight_people)

#Printing list in order original
print("List of weight peoples: ",list_people_weight)
print("List of hight peoples: ",list_people_hight)

#Printing in order reverse without function
print("List of weight peoples reverse: ",list_people_weight[::-1])
print("List of hight peoples reverse: ",list_people_hight[::-1])

#Printing in order reverse with function
list_people_weight.reverse()
list_people_hight.reverse()
print("List of weight peoples reverse: ",list_people_weight)
print("List of hight peoples reverse: ",list_people_hight)
