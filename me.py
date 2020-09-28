#List
counties=["Arapahoe","Denver","Jefferson"]
print(counties[0])
#find length of list
print(len(counties))
#Slice List
print(counties[0:2])
print(counties[:2])
print(counties[1:])

#add Items to List
counties.append("El Paso")
print(counties)

#add item/select place
counties.insert(1 ,"nakanishi")
print(counties)
#remove - remove
counties.remove("nakanishi")
print(counties)
#remove - pop
counties.pop(3)
print(counties)
#change element in List
counties[2]="El Paso"
print(counties)
#Tuple are similar to lists in Python but cannot be changed/added/removed - called immutable
counties_tuple=("Arapahoe","Denver","Jefferson")
print(counties_tuple[1])
#Dictionary is an object that stores a collection of data. Dictionary has a key and a value or key-value pairs.
#{key1:value1,key2:value2}
#values in a dictionary can be objects of any type. Key must be immutable objjects like integer, floating...etc cannot be lists or any other type pf mutable object.

#Create a Dictionary
#my_dictionary={}
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432338
print(counties_dict)
#get Length of dictionary
len(counties_dict)
#item() ---- to get all the keys and values printed to the screen -- known as view object. You cannot use list indexing with items() method
print(counties_dict.items())
#keys() - to get only the keys from dictionary
print(counties_dict.keys())
#values() - to get only the values from dictionary
print(counties_dict.values())
#get() - to get a specific value
print(counties_dict.get("Denver"))
#dictonary_name[key] - write the key within "" or '' to get value by the name
print(counties_dict["Arapahoe"])
#List of dictionaries [{key1:value1,key2:value2},{key1:value3,key2:value4}] - each dictionary is wrapped in brackets
voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
#input function - ask user to enter 
#int - converts the user input value to an integer
#float - convert to float
#str - convert to string

#Decision Statement - If...Else
counties=['Arapahoe', 'Denver', 'Jefferson']
if counties[1] == 'Denver': #-------  != means not equal to
    print(counties[1])
#be careful with indent
temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print ("Turn on the AC")
else:
    print("Open the window")
#nested if-Else
score = int(input("What is your test score?"))

if score > 90:
    print('Your grade is A.')
else:
    if score >80:
        print('Your grade is B.')
    else:
        if score > 70:
            print('Your grade is C.')
        else:
            if score > 60:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
#elif-else
score = int(input("What is your test score?"))

if score>90:
    print('Your grade is A.')
elif score>80:
    print('Your grade is B.')
elif score >70:
    print('Your grade is C.')
elif score>60:
    print('Your grade is D.')
else:
    print('Your grade is F.')
#membership operators
## 'in and 'not in' ---- this prints "True"/"False"
counties = ["Arapahoe","Denver","Jefferson"] 
if "Arapahoe" in counties:
    print("True") 
else: 
    print("False")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#Logical Operator - "and" "or" "not" --- will retun "True"/"Faluse"
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
#Loop
###Conditional-controlled loop ---- while loop ---- true or false condition to control the number of times that it repeats
x = 0
while x <= 5:
    print(x)
    x = x + 1
###Count-Controlled loop ---- for loop -----repeat specif number of times depending on conditions
####for item in [items]:
#####    statement 1
#####    statement 2
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
#same result
for num in range(5):
    print(num)

#get the length of list and use range so that it will loop for as long as list last.
for i in range(len(counties)):
    print(counties[i])
#get Key from Fictionary
counties_dict={'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432338}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
#get value from Dictionary
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict['Arapahoe'])
for county in counties_dict:
    print(counties_dict.get(county))
#to get key-value pairs of dictionary
#for key, value in dictionary_name.items():
for county,voters in counties_dict.items():
    print(county,voters)
#get each dictionary in a list of dictionary
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
#nest for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#print Function
##Print() and print(""+"")

#f-string used in place of concatenation 
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100:.2f}% of the total votes.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#formatting floating-points
##f'{value:{width},.{precision}}'
