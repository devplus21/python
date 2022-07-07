# access value of dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name']) # dict['Name']: Zara
print("dict['Age']: ", dict['Age']) # dict['Age']: 7


# Updating Dictionary
dict['Age'] = 8
dict['School'] = "DPS School"

print("dict['Age']: ", dict['Age']) # dict['Age']: 8
print("dict['School']: ", dict['School']) # dict['School']: DPS School
print(dict) # {'Name': 'Zara', 'Age': 8, 'Class': 'First', 'School': 'DPS School'}


# Delete Dictionary Elements
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
