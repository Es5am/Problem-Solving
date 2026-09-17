"""
Problem 1 : What Is The Data Type Of The Following Values ( 1 , 0.6 , 5+6j ) ?

Problem 2 : Create A Variable Called ( c ) And Assign It With A Complex Number, Then Print The Imaginary And Real Parts Of It.

Problem 3 : Create A Variable Called ( num ) And Assign It With A Number, Then Print The Number With 10 Decimal Points.

Problem 4 : Create A Variable Called ( num ) And Assign It With A Number, Then Print The Number After Converting It To An Integer.

Problem 5 : Print The Results Of The Following Operations ( 100-115 , 50*30 , 22 % 4 , 110/11 , 97//20 ) Using ( print ).

"""
#                         Solution
##################################_Ass-1_##################################

print(type(1))
print(type(0.6))
print(type(5+6j))

##################################_Ass-2_##################################

c=1+2j
print("The Imaginary Part Is: {}".format(c.imag))
print("The Real Part Is: {}".format(c.real))

##################################_Ass-3_##################################

num = 10
print("{:.10f}".format(num))

##################################_Ass-4_##################################

num = 159.650
print(int(num))
print(type(int(num)))

##################################_Ass-5_##################################

print(100-115)
print(50*30)
print(22 % 4)
print(int(110/11))
print(97 // 20)