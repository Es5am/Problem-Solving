"""
Problem 1: Check If All Values In The List Are True Or Not Using ( all() ) Function, And Check If Any Value In The List Is True Or Not Using ( any() ) Function.

Problem 2: Create A List From ( 0 ) To ( 40 ) And Return The Total Of All Numbers In The List Using ( sum() ) Function, And Return The Total Of All Numbers In The List Using ( pow() ) Function.

Problem 3: Create A List From ( 0 ) To ( 21 ) And Return The Average Of All Numbers In The List Using ( sum() ) Function, And Return The Maximum Number In The List Using ( max() ) Function.

Problem 4: Create Your Own Functions Called ( my_all() ) And ( my_any() ) That Work Like The Built-in Functions ( all() ) And ( any() ) Respectively,
And Create Your Own Functions Called ( my_min() ) And ( my_max() ) That Work Like The Built-in Functions ( min() ) And ( max() ) Respectively.

"""

#                         Solution




######################### Ass_1 ####################

values = (0, 1, 2)

if any(values):# لازم كل القيم تكون صحيحه

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):# هيطبع good علشان اول واحده شرط تحقق وor محتاجه واحد على الاقل

  print("Good")

else:

  print("Bad")


print("-"*50)

######################### Ass_2 ####################


v = 40 

my_range = list(range(v))


#مجموع الارقام من اول 0 لحد 40 نجمعها اما بالنسبه لقيمه الدالهpow(v, v, v)) دي بتساوي صفر مع اى رقم في الدنيا 
# حسبناها من قانون (x/2)*(x+1) = 820 
print(sum(my_range, v) + pow(v, v, v))  # 820


print("-"*50)
######################### Ass_3 ####################

n = 21 # ((n-1)/2)*(n-1+1)) / n = 10 -> (((n-1)/2)*(n))/n
       # (n-1/2) = 10 -> n = (10*2+1)

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

print("-"*50)

######################### Ass_4 ####################

def my_all(iterable):
    for element in iterable:
        if not element:  
            return False
    return True


def my_any(iterable):
    for element in iterable:
        if  element:  
            return True
    return False


def my_min(iterable):
   minmum=iterable[0]
   for element in iterable:
      if element < minmum:
         minmum=element
   return minmum


def my_max(iterable):
   maxmum=iterable[0]
   for element in iterable:
      if element > maxmum:
         maxmum=element
   return maxmum


# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False
print("-"*50)

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False
print("-"*50)

# my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100
print("-"*50)

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700
print("-"*50)

