"""
Problem 1: Create a generator function that reverses a string.

Problem 2: Create a decorator that adds sugar to tea and coffe. The decorator should print "Sugar Added From Decorators" before the function call and print "####################" after the function call.

Problem 3: Use the re module to find all the words that end with a specific letter in a given string. Print the results.

Problem 4: Use the re module to find all the words that start with a specific letter in a given string. Print the results.

Problem 5: Use the re module to find all the phone numbers in a given string that match a specific pattern. Print the results.
"""
#                         Solution

############################## Ass_1 ##############################

import re

string_one = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "

search_one = re.findall(r"(\w\b)",string_one) # \w for string , \b for end of word

for word in search_one :
    print(word , end=" ")

print() # for new line

print( '-' * 50 ) # => Seprator

############################## Ass_2 ##############################

string_two = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"

search_two = re.findall(r"L[A-z]+",string_two)

for word in search_two :
    print(word , end=" ")

print() # for new line

print( '-' * 50 ) # => Seprator

############################## Ass_3 ##############################

nums = """+(0100) 600-1234
          +(0100) 60-1234
          (0100) 6000-1234
          01006001234
          0100 600 1234
          (0100) 600-1
          (0100) 600-12"""


search_three = re.findall(r"\+?\(\d+\)\s\d+-\d{4}",nums)


for word in search_three :
    print(word)

print( '-' * 50 ) # => Seprator

############################## Ass_4 ##############################

links = """http://www.elzero.org:8888/link.php
           https://elzero.org:8888/link.php
           http://www.elzero.com/link.py
           https://elzero.com/link.py
           http://www.elzero.net
           https://elzero.net"""

search_four = re.findall(r"(https?)://(www)?.?(\w+).(com|org)(.+)",links)

for word in search_four :
    
    result_string= " ".join(word)
    print(result_string)

print( '-' * 50 ) # => Seprator

############################## Ass_5 ##############################

string_five = """http
                 https
                 abcd
                 abcd"""

first_way = re.findall(r"(https?)",string_five)
second_way = re.findall(r"(https|http)",string_five)
third_way = re.findall(r"http[s]?",string_five)
fourth_way = re.findall(r"https{0,1}",string_five)
fifth_way = re.findall(r"\bhttps?\b",string_five)


print("First Way : ")

for word in first_way :
    print(word)

print( '-' * 50 ) # => Seprator

print("Second Way : ")

for word in second_way :
    print(word)

print( '-' * 50 ) # => Seprator

print("Third Way : ")

for word in third_way :
    print(word)

print( '-' * 50 ) # => Seprator

print("Fourth Way : ")

for word in fourth_way :
    print(word)

print( '-' * 50 ) # => Seprator

print("Fifth Way : ")

for word in fifth_way :
    print(word)

print( '-' * 50 ) # => Seprator



