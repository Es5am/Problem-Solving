"""
Problem 1: Create a generator function that reverses a string.
Problem 2: Create a decorator that adds sugar to tea and coffe. The decorator should print "Sugar Added From Decorators" before the function call and print "####################" after the function call.


"""
#                         Solution

############################## Ass_1 ###################################



def reverse_string(my_string):
  
  for i in  range(len(my_string)-1,-1,-1):
    yield my_string[i]

for c in reverse_string("Elzero"):
  print(c)

print("-"*50)
############################## Ass_2 ###################################


def decorator(function):
  def targeted():
    print("Sugar Added From Decorators")
    function()
    print("#"*20)
  return targeted 

@decorator
def make_tea():
  print("Tea Created")

@decorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()



