"""
Problem 1 : Test the following assertions using the unittest module:
- Check if the number 10 is in the list [5, 7, 8, 10].
- Check if the number 10 is an instance of the int type.
- Check if the value 100 is True.
- Check if the empty list [] is False.
- Check if the number 100 is greater than or equal to 90.

Problem 2 : Create a function called make_serial that generates a random serial number in the format XXXX-XXXX-XXXXXX, where X can be any uppercase letter, lowercase letter, or digit.
Use the random and string modules to generate the serial number. Print the generated serial number.


"""

#                         Solution

############################## Ass_1 ##############################

import unittest

class MyTestCase(unittest.TestCase):
    
    
    def test_one(self):
        self.assertIn(10, [5, 7, 8, 10])
        
    
    def test_two(self):
        self.assertIsInstance(10, int)
        
    
    def test_three(self):
        self.assertTrue(100)
        
   
    def test_four(self):
        self.assertFalse([])
        
    
    def test_five(self):
        self.assertGreaterEqual(100, 90)


if __name__ == "__main__":
    unittest.main()

print( '-' * 50 ) # -> Separetor

############################## Ass_2 ##############################

import string
import random

def make_serial():
    
    all_chars = string.ascii_letters + string.digits
    
    part1 = "".join(random.choices(all_chars, k=4))
    part2 = "".join(random.choices(all_chars, k=4))
    part3 = "".join(random.choices(all_chars, k=6))

    return f"{part1}-{part2}-{part3}"


print(make_serial())
print(make_serial())


""" Make By EM7 Best Wish For EveryOne Who Complete This Course Please Don't Stop Keep Moving You Are The Best """