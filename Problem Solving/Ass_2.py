"""
Problem 1 : Create A Variables Called ( Name , Age , Country ) And Assign Values To It, Then Print The Variables In One Line Using (%S).

Problem 2 : Create A Variables Called ( Name , Age , Country ) And Assign Values To It, Then Print The Variables In One Line Using (%S) With New Line.

Problem 3 : Create A Variable Called ( name ) And Assign A String Value To It, Then Print The Characters Of The Variable ( name ) Using Indexing.

Problem 4 : Create A Variable Called ( name ) And Assign A String Value To It, Then Print The Characters Of The Variable ( name ) Using Slicing.

Problem 5 : Create A Variable Called ( name ) And Assign A String Value To It, Then Print The Variable ( name ) After Removing The Characters (#@) From It.

Problem 6 : Create A Variables Called ( a , b , c , d , f ) And Assign Values To It, Then Print The Variables ( a , b , c , d , f ) After Adding Zeros To The Left Of Each Variable Using ( zfill ).

Problem 7 : Create A Variables Called ( name_one , name_two ) And Assign Values To It, 
Then Print The Variables ( name_one , name_two ) After Adding Characters To The Left Of Each Variable Using ( ljust , rjust ).

Problem 8 : Create A Variables Called ( name_one , name_two ) And Assign Values To It, Then Print The Variables ( name_one , name_two ) After Swapping The Case Of Each Variable Using ( swapcase ).

Problem 9 : Create A Variable Called ( msg ) And Assign A String Value To It, Then Print The Number Of Occurrences Of A Specific Word In The Variable ( msg ) Using ( count ).

Problem 10 : Create A Variable Called ( name ) And Assign A String Value To It, Then Print The Index Of A Specific Character In The Variable ( name ) Using ( index ).

Problem 11 : Create A Variable Called ( msg ) And Assign A String Value To It, Then Print The Variable ( msg ) After Replacing A Specific Word In It Using ( replace ) With One Occurrence.

Problem 12 : Create A Variable Called ( msg ) And Assign A String Value To It, Then Print The Variable ( msg ) After Replacing A Specific Word In It Using ( replace ) With All Occurrences.

Problem 13 : Create A Variables Called ( name , age , country ) And Assign Values To It, Then Print The Variables ( name , age , country ) Using ( f-string ).

"""
#                         Solution

##################################_Ass-1_##################################

Name="'Essam'"
Age='"20"'
Country="Egypt"
print('Hello %s , How You Doing \\""" Your Age Is %s" + And Your Country Is: %s'%(Name,Age,Country))
print("-"*50)

##################################_Ass-2_##################################

Name="'Essam'"
Age='"20"'
Country="Egypt"
print('Hello %s , How You Doing \\\n""" Your Age Is %s" + \n And Your Country Is: %s'%(Name,Age,Country))
print("-"*50)

##################################_Ass-3_##################################

name='Elzero'
print(name[1])
print(name[2])
print(name[5])
print("-"*50)

##################################_Ass-4_##################################

name='Elzero'
print(name[1:4])
print(name[::2])
print(name[-2::-2])
print("-"*50)

##################################_Ass-5_##################################

name = "#@#@Elzero#@#@"
print(name.strip("#@"))
print("-"*50)

##################################_Ass-6_##################################

a,b,c,d,f="9","15","130","950","1500"
print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))
print(f.zfill(4))
print("-"*50)

##################################_Ass-7_##################################

name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.ljust(20,"@"))
print(name_two.rjust(20,"@"))
print("-"*50)

##################################_Ass-8_##################################

name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

print("-"*50)
##################################_Ass-9_##################################

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))
print("-"*50)

##################################_Ass-10_##################################

name="Elzero"
print(name.index("z"))
print("-"*50)

##################################_Ass-11_##################################

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","love",1))
print("-"*50)

##################################_Ass-12_##################################

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love"))
print("-"*50)

##################################_Ass-13_##################################

name = "Essam"
age = 20
country = "Egypt"
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
print("-"*50)