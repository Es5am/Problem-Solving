"""

Problem 1 : Create A Simple Calculator That Takes Two Numbers And An Operation From The User And Print The Result Of The Operation, If The User Entered An Invalid Operation Print Error Message.

Problem 2 : Create A Variable Called ( age ) And Assign It With The User Age, Then Print The Result Of The Following Expression ( age > 16 ) If The Result Is True Print ( App Is Suitable For You ) Else
Print ( App Is Not Suitable For You ).

Problem 3 : Create A Variable Called ( age ) And Assign It With The User Age, Then Print The Result Of The Following Expression ( age > 10 and age < 100 ) If The Result Is True Print
( You Lived For : ) And Print The User Age In Months , Weeks , Days , Hours , Minutes , Seconds Else Print ( Out Of Range ).


Problem 4 : Create A Variable Called ( country ) And Assign It With The User Country, Then Create A List Called ( countries ) And Assign It With Some Countries,
Then Create Two Variables Called ( price , discount ) And Assign Them With Some Values, Then Print The Result Of The Following Expression ( country in countries )
If The Result Is True Print ( Your Country Eligible For Discount And The Price After Discount Is ${price-discount}. ) Else Print ( Your Country Not Eligible For Discount And The Price Is ${price}. )


"""
#                         Solution


######################## Ass_1 ########################

num1 = int(input("Please Enter The First Number : ").strip())
num2 = int(input("Please Enter The Second Number : ").strip())
operation = input("Please Enter The Operation : ").strip()

if operation == "+" or operation == "Plus" :
 print(f"The Result Is = {num1+num2}")
elif operation == "-" or operation == "Minus" :
 print(f"The Result Is = {num1-num2}")
elif operation == "*" or operation == "Multipler" :
 print(f"The Result Is = {num1*num2}")
elif operation == "**" or operation == "Expontial" :
 print(f"The Result Is = {num1**num2}")
elif operation == "/" or operation == "Division" :
 print(f"The Result Is = {num1/num2}")
elif operation == "%" or operation == "Qoution" :
 print(f"The Result Is = {num1%num2}")
else: print("Error")

print("=" * 50)

######################## Ass_2 ########################

age = int(input("Please Enter Your Age : "))
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")

print("=" * 50)

######################## Ass_3 ########################

age = int(input("Please Enter Your Age : "))

month = age *12
weeks = month*4
days = age*365
hours = days*24
minutes = hours * 60
seconds = minutes * 60

if age > 10 and age < 100 :
 print("You Lived For : ")
 print(f"{month} Months")
 print(f"{weeks:,} Weeks")
 print(f"{days:,} Days")
 print(f"{hours:,} Hours")
 print(f"{minutes:,} Minutes")
 print(f"{seconds:,} Seconds")

else :
 print("Out Of Range")

print("=" * 50)

######################## Ass_4 ########################

country = input("Please Enter Your Country : ").capitalize().strip()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "Ksa", "Usa", "Bahrain", "England"]
price = 100
discount = 30

if country in countries :
 print(f"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}.")
else :
 print(f"Your Country Not Eligible For Discount And The Price Is ${price}.")

print("=" * 50)
