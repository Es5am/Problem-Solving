

"""
Problem 1 : Print The Boolean Value Of The Following Values ( True , "Essam" , 100 , [1, 2] ) And Print The Boolean Value Of The Following Values ( False , "" , 0 , [] )

Problem 2 : Create Three Variables Called ( html , css , javascript ) And Assign Them With Some Values, Then Print The Result Of The Following Expression ( html > 50 and css > 50 and javascript > 50 ).

Problem 3 : Create Three Variables Called ( num_one , num_two , num ) And Assign Them With Some Values, Then Print The Result Of The Following Expression ( num > num_one or num > num_two )
And Print The Result Of The Following Expression ( num > num_one and num > num_two ).

Problem 4 : Create Two Variables Called ( num_one , num_two ) And Assign Them With Some Values, Then Create A Variable Called ( result ) And Assign It With The Result Of The Following Expression 
( num_one + num_two ),Then Use The Compound Assignment Operators To Do The Following Operations On The Variable ( result ) In The Following Order ( Exponentiation , Modulus , Division ), Then Print The Result And Its Type.

"""
#                         Solution


######################################## Ass_1 ########################################

print(bool(True))
print(bool("Essam"))  
print(bool(100))      
print(bool([1, 2]))

print("="*50)

print(bool(False))
print(bool(""))  
print(bool(0))      
print(bool([])) 

print("="*50)

######################################## Ass_2 ########################################

html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)

print("="*50)


######################################## Ass_3 ########################################

num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

print("="*50)

######################################## Ass_4 ########################################

num_one = 10
num_two = 20
result = num_one + num_two
print(result)
result**= 3
print(result)
result%=26000
print(result)
result/=5
print(result)
print(type(str(result)))