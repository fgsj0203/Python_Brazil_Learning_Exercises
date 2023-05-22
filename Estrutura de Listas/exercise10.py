"""
Creating list of input age and hight and calculate average hight of peoples
"""

#Creating list empty
hight_people_list = []
age_people_list = []
age_hight_people_down = []
#Calculating and iteration of data age and hight
for x in range(0,2):
    hight = float(input("Enter with a hight: ")) #Variable for addition in list hight people
    hight_people_list.append(hight)
    age = int(input("Enter with a age: "))
    age_people_list.append(age)


#Printing list final hight and age
print("List of hight: ",hight_people_list)
print("List of age: ",age_people_list)

hight_average = 0
for x in (hight_people_list):
    hight_average = hight_average + x

#Calculating average hight people
average_hight_final = hight_average/2
print(average_hight_final)

for x in hight_people_list:
    if (x < average_hight_final):
        age_hight_people_down.append(x)

print("List final of peoples with down age 13 and hight average",age_hight_people_down)


