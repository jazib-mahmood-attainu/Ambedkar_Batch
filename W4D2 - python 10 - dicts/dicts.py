"""
Dictionary - is another type of DS
property 1:
Syntax
for indexing we use key:value pair in the form of
{
    key1:value1,
    key2:value2,
    .
    .
    .
}


property 2:
you can have, 
integer/float/string/list/tuple/anotherdictionary
 as a value inside a dictionary

property 3:
Keys should never repeat/keys are always unique for a dictionary

property 4:
to change a previous value
dict_name[key] = new_value

property 5:
to add a  value
dict_name[new_key] = new_value

property 6:
to remove a key,value pair
dict_name.pop(key)

APIs:
1. .keys()
2. .values()
"""

height = {
            "Amar":5.8,
            "Ankit": 6.1,
            "Preeti": 5.5,
            "Jazib":5.3,
            "Kanhu":6.11,
            

}

# home_town = {
#             "Amar":"Delhi",
#             "Jazib":"Gorakhpur",
#             "Govind":"Gorakhpur",
#             "Sanjeet":"Gorakhpur",
#             "Ankit":["Patna","Bihar"],
#             "Biswajit":{"state":"Orissa","city":"Bhumbhneshwar"}

# }

print(height["Amar"])
height["Amar"] = 6.2
print(height["Amar"])

height["Rajnish"] = 5.8
print(height["Rajnish"])

# print(height["sapna"])
# print(home_town["Ankit"][0])
# print(home_town["Biswajit"])


height.pop("Jazib")
print(height)

print(len(height.keys()))
print(height.values())
