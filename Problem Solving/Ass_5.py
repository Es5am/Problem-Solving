"""
Problem 1 : Create A Variable Called ( name ) And Assign It With Your Name, Then Print The Variable ( name ) And Its Type.

Problem 2 : Create A Tuple Called ( friends ) And Assign It With Some Names, Then Print The Tuple ( friends ) And Its Type,
Then Add Your Name To The Tuple ( friends ) And Print It Again With Its Type, Then Print The Length Of The Tuple ( friends ) Using ( f-string ).

Problem 3 : Create A Tuple Called ( nums ) And Assign It With Some Numbers, Then Create Another Tuple Called ( letters ) And Assign It With Some Letters,Then Create A New Tuple Called 
( nums_and_letters_one ) And Assign It With The Concatenation Of The Two Tuples ( nums , letters ), Then Print The New Tuple ( nums_and_letters_one ) And Its Length Using ( f-string ).

Problem 4 : Create A Tuple Called ( my_tuple ) And Assign It With Some Values, Then Unpack The Tuple Into Four Variables ( a , b , _ , c ) And Print The Variables ( a , b , c ).
"""


#                         Solution


##################### Ass_1 ########################

name = "Essam",
print(name)
print(type(name))
print("-"*50)

##################### Ass_2 ########################

friends = ("Osama","Ahmed","Sayed")
friends = ("Elzero",) + friends[1:]
print(friends)
print(type(friends))
print(f"{len(friends)} Elements")
print("-"*50)

##################### Ass_3 ########################

nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(f"{len(nums_and_letters_one)} Elements")
print("-"*50)

##################### Ass_4 ########################

my_tuple = (1, 2, 3, 4)
a,b,_,c = my_tuple
print(a)
print(b)
print(c)
print("-"*50)