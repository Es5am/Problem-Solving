"""
Problem Solving Assignment 10

Problem 1 : Get A Number From User And Print All Numbers From This Number To 1, If The Number Is Not Larger Than 0 Print ( The Number {num} Is Not Larger Than 0 ) And Print The Count Of Numbers Printed Successfuly.

Problem 2 : Create A List Called ( friends ) And Assign It With Some Names, Then Print All Names That Start With Capital Letter And Print The Count Of Ignored Names.

Problem 3 : Create A List Called ( skills ) And Assign It With Some Skills, Then Use The While Loop To Print All Skills In The List.

Problem 4 : Create An Empty List Called ( my_friends ) And Create A Variable Called ( max_friends ) And Assign It With The Maximum Number Of Friends Allowed,
Then Use The While Loop To Get Friends Names From User And Add Them To The List Until The Length Of The List Is Equal To The Maximum Number Of Friends Allowed,
If The User Entered A Name In Uppercase Print ( Invalid Name ), If The User Entered A Name In Lowercase Add It To The List And Print ( Friend {name} Added => 1st Letter Become Capital )
And Print The Count Of Names Left In List, If The User Entered A Name With First Letter Capitalized Add It To The List And Print ( Friend {name} Added ) And Print The Count Of Names Left In List.
"""
#                         Solution



######################### Ass_1 #########################

num = int(input("Please Enter A Number : ")) 
if num > 0 :
 count=0
 while num > 1 :
  num-=1
  if num !=6 :
   print(num)
   count+=1
else:
 print(f"The Number {num} Is Not Larger Than 0")
print(f"{count} Numbers Printed Successfuly")

print("="*50)

######################### Ass_2 #########################

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
index = 0
count=0
while index < len(friends) :
 
 if friends[index][0].isupper() :
    print(friends[index])
 else: 
    count+=1
 index+=1  

print(f"Friends Printed And Ignored Names Count Is {count}")

print("="*50)

######################### Ass_3 #########################

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
 print(skills.pop(0))

print("="*50)

######################### Ass_4 #########################

my_friends = []
max_friends = 4

while len(my_friends) < max_friends :
  name = input("Please Enter Add Your Friend : ").strip() 

  if name.isupper():
   print("Invalid Name")

  elif name.islower():
   my_friends.append(name)
   print(f"Friend {name.capitalize()} Added => 1st Letter Become Capital")
   print(f"Names Left in List Is {max_friends-len(my_friends)}")
   
  elif name[0].capitalize :
   my_friends.append(name)
   print(f"Friend {name} Added")
   print(f"Names Left in List Is {max_friends-len(my_friends)}")

print(my_friends)