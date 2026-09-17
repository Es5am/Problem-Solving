"""
Problem 1 : Create A List Called ( my_list ) And Assign It With Some Values, Then Create A New List Called ( unique_list ) And Assign It With The Values Of The First List Without Any Repeated Values,
Then Print The New List ( unique_list ) And Its Type, Then Print The First Four Values Of The New List ( unique_list ).

Problem 2 : Create A Set Called ( nums ) And Assign It With Some Numbers, Then Create Another Set Called ( letters ) And Assign It With Some Letters, Then Print The Union Of The Two Sets ( nums , letters ) 
Using Two Different Methods, Then Update The First Set ( nums ) With The Values Of The Second Set ( letters ) And Print The First Set ( nums ).

Problem 3 : Create A Set Called ( my_set ) And Assign It With Some Values, Then Clear The Set ( my_set ) And Print It, 
Then Add Two New Values To The Set ( my_set ) And Discard One Value From It,Then Print The Set ( my_set ).

Problem 4 : Create A Set Called ( set_one ) And Assign It With Some Values, Then Create Another Set Called ( set_two ) And Assign It With Some Values,
Then Print If The First Set ( set_one ) Is A Subset Of The Second Set ( set_two ).

Problem 5 : Create A Dictionary Called ( skills ) And Assign It With Some Key/Value Pairs, Then Add A New Key/Value Pair To The Dictionary ( skills ), 
Then Print The Values Of Each Key In The Dictionary ( skills ) Using ( f-string ).


"""
#                         Solution

######################################## Ass_1 ####################################

my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = my_list [0:3] + my_list [4:6]
print (unique_list)
print(type(unique_list))
print(unique_list[:4])
print("-"*50)

######################################## Ass_2 ####################################

nums = {1, 2, 3}
letters = {"A", "B", "C"}
print (nums.union(letters))
print (nums|letters)
nums.update(letters)
print(nums)
print("-"*50)

######################################## Ass_3 ####################################

my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
my_set.discard("C")
print(my_set)
print("-"*50)

######################################## Ass_4 ####################################

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print("-"*50)

######################################## Ass_5 ####################################

skills = {
    "Html":"90%",
    "Css" :"80%",
    "Python":"30%",
}

skills ["Ai"] = "20%"

print(f"HTML Progress is {skills['Html']}")
print(f"CSS Progress is {skills['Css']}")
print(f"Python Progress Is {skills['Python']}")
print(f"AI Progress Is {skills['Ai']}")

print("-"*50)