"""
Problem 1: Use map to remove the first and last characters of each name in the list friends_map.

Problem 2: Use filter to get the names that end with the letter "m" from the list friends_filter.

Problem 3: Use reduce to multiply all the numbers in the list nums.

Problem 4: Use enumerate to print the skills in the list skills along with their index, starting from 50. Skip any skills that are not strings.
"""

#                         Solution


######################## Ass_1 ########################

from functools import reduce


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

def remove_chars (char):
    return char [1:-1]

cleaned_list = map(remove_chars ,friends_map)

for clean_name in cleaned_list:
    print(clean_name)

print("-"*50)

for clean_name in map( lambda char : char[1:-1],friends_map):
    print(clean_name)

print("-"*50)

######################## Ass_2 ########################

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names (word):
    return word.endswith("m")

names = filter(get_names,friends_filter)

for name in names:
    print(name)

print("-"*50)

for name in filter( lambda word : word.endswith("m"),friends_filter):
    print(name)

print("-"*50)

######################## Ass_3 ########################

def multi(num1,num2):
    return num1*num2

nums = [2, 4, 6, 2]

result = reduce(multi,nums)

print(result)

print("-"*50)

print(reduce(lambda num1,num2 : num1*num2, nums ))

print("-"*50)

######################## Ass_4 ########################

skills = reversed(("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript"))


myskills = enumerate(skills,50)
for counter,skill in myskills:

    if isinstance(skill, int):
        continue
    print(f"{counter} - {skill}")

print("-"*50)


for counter,skill in enumerate(reversed(("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")),50):

    if type(skill) == int:
        continue
    print(f"{counter} - {skill}")

print("-"*50)


for counter,skill in enumerate(reversed(("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")),50):

    if type(skill) == str:
        print(f"{counter} - {skill}")
        


