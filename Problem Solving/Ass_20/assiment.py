"""
This module allows you to say hello to a list of friends.
"""

my_friends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples):
    """
    This function says hello to each person in the list.
    """
    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(my_friends)
