"""
Calculate tax of market of fish
"""

#Received of weight fish
weightFish = float(input("Enter with weight fish in KG: "))


#Create condition of payment tax
if(weightFish > 50):
    excessWeightFish = (weightFish - 50)
    valueTaxFish = excessWeightFish * 4
    print("You payment tax of excess weight fish: R$ ",valueTaxFish )
else:
    print("You isent of payment tax weight fish")