#Exercises 1-10 found on https://pynative.com/python-dictionary-exercise-with-solutions/#h-exercise-1-convert-two-lists-into-a-dictionary
#not used yet: https://learnpython.com/blog/python-dictionary-exercises/
#not used yet: https://www.geeksforgeeks.org/python-dictionary-exercise/

#Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
newdict = {keys[i]:values[i] for i in range(len(keys))}
print(newdict)

#Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

#Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict.get('class', {}).get('student', {}).get('marks', {}).get('history'))

#Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
default = dict.fromkeys(employees, defaults)
print(default)

#Exercise 5: Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

extract = {k:sample_dict.get(k) for k in keys}
print(extract)


#Exercise 6: Delete a list of keys from a dictionary
sample_dict = {
    "name": 4,
    "age": 25,
    "salary": 8000,
    "city": 7
}

# Keys to remove
keys = ["name", "salary"]
print(list(sample_dict))
for k in keys:
    sample_dict.pop(k)

#oder
sample_dict1 = {k: sample_dict[k] for k in (sample_dict.keys() - keys)}

sample_dict2 = {k if len(k)>4 else 'dummy': sample_dict[k] if sample_dict[k]%2!=0 else 'even' for k in sample_dict}

def mypair(k):
    if sample_dict[k]%2!=0:
        return sample_dict[k]
    else:
        return 'even'

sample_dict3 = {k: mypair(k) for k in sample_dict if k not in keys}

print(sample_dict2)
print(sample_dict3)
#Exercise 7: Check if a value exists in a dictionary
value = 200
sample_dict = {'a': 100, 'b': 200, 'c': 300}
print(value in sample_dict.values())


#Exercise 8: Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
#rename 'city' to 'location'
sample_dict['location'] = sample_dict.pop('city') #returns value of 'city'
#sample_dict[key] = value
print(sample_dict)

#Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sample_dict, key=sample_dict.get)) #The key parameter allows you to specify a function that determines the value used for comparison. #example: len to compare by length
print(max(sample_dict, key=sample_dict.get))


#Exercise 10: Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)



sample_list = [-15,2,3]
print(min(sample_list))
print(min(sample_list, key = lambda x: x**2))
print(min(map(lambda x: x**2, sample_list)))
