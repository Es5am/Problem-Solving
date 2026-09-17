"""
Problem 1: Use the random module to generate a random number between 10 and 50, a random even number between 2 and 10, and a random odd number between 1 and 9. Print the results.

Problem 2: Create a module named my_mod.py that contains two functions: say_hello(name) and say_welcome(name). Import the module and call both functions with the name "Osama".

Problem 3: Import only the say_welcome function from the my_mod module and call it with the name "Osama".

Problem 4: Import the say_welcome function from the my_mod module and give it an alias new_welcome. Call the new_welcome function with the name "Osama".
"""

#                         Solution

#################################### Ass_1 ###########################


from random import *

rndm = randint(10,50)
num_even = randrange(2,10,2)
num_odd = randrange(1,9,2)

print(f"Random Number Between 10 And 50 => {rndm}" )
print(f"Random Even Number Between 2 And 10 => {num_even}" )
print(f"Random Odd Number Between 1 And 9 => {num_odd}" )

print(dir(random))

print("-"*50)

#################################### Ass_2 ###########################

import my_mod

my_mod.say_hello("Osama")
my_mod.say_welcome("Osama")

#################################### Ass_3 ###########################

from my_mod import say_welcome
say_welcome("Osama")

#################################### Ass_4 ###########################

from my_mod import say_welcome as new_welcome
new_welcome("Osama")
