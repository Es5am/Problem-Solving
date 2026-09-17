"""
Problem 1 : Create A List Called ( friends ) And Assign It With Some Names, Then Print The First Name, Last Name, And The Name At Index 2.

Problem 2 : Create A List Called ( friends ) And Assign It With Some Names, Then Print The Names At Even Indexes, And The Names At Odd Indexes.

Problem 3 : Create A List Called ( friends ) And Assign It With Some Names, Then Print The Names From Index 1 To Index 3, And The Names From Index 3 To The End Of The List.

Problem 4 : Create A List Called ( friends ) And Assign It With Some Names, Then Replace The Names From Index 3 To The End Of The List With ( Elzero , Elzero ) And Print The List.

Problem 5 : Create A List Called ( friends ) And Assign It With Some Names, Then Add A Name At The Beginning Of The List, And Add Another Name At The End Of The List, Then Print The List.

Problem 6 : Create A List Called ( friends ) And Assign It With Some Names, Then Remove The First Name, And Remove The Last Name, Then Print The List.

Problem 7 : Create A List Called ( friends ) And Assign It With Some Names, Then Create Another List Called ( employees ) And Assign It With Some Names,Then Create Another List Called
( school ) And Assign It With Some Names, Then Add The ( employees ) List To The ( friends ) List, And Add The ( school ) List To The ( friends ) List, Then Print The List.

Problem 8 : Create A List Called ( friends ) And Assign It With Some Names, Then Sort The List In Ascending Order, Then Sort The List In Descending Order, Then Print The List.

Problem 9 : Create A List Called ( friends ) And Assign It With Some Names, Then Print The Length Of The List.

Problem 10 : Create A List Called ( technologies ) And Assign It With Some Values, Then Print The First Value, The Last Value, And The Type Of The List.

"""
#                         Solution

###################### Ass_1 ########################

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])
print("-"*50)

###################### Ass_2 ######################## 

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1:4:2])
print("-"*50)

###################### Ass_3 ########################

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[3:])
print("-"*50)

###################### Ass_4 ########################

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends[3:]=("Elzero","Elzero")
print(friends)
print("-"*50)

###################### Ass_5 ########################

friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,"Nasser")
friends.append("Salem")
print(friends)
print("-"*50)

###################### Ass_6 ########################

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.remove("Nasser")
friends.remove("Osama")
print(friends)
friends.remove("Salem")
print(friends)
print("-"*50)

###################### Ass_7 ########################

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)
print("-"*50)

###################### Ass_8 ########################

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
print("-"*50)

###################### Ass_9 ########################

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))
print("-"*50)

###################### Ass_10 ########################

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][2])
print(type(technologies))
print("-"*50)
