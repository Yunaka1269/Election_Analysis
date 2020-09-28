counties = ["Arapahoe","Denver","Jefferson"]

if counties[1]=='Denver':
    print(counties[1])


counties = ["Arapahoe","Denver","Jefferson"]

#if "El Paso" in counties:
#    print("Els Paso is in the list of counties")
#else:
#    print("El Paso is not in the list of counties")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")

counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)




