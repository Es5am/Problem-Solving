"""

Problem 1 : Get User Name And Print Welcome Message

Problem 2 : Get User Age And Print Message If Age Is Under 16 Or Not

Problem 3 : Get User First Name And Middle Name And Print First Name With First Letter Of Middle Name

Problem 4 : Get User Email And Print User Name, Email Service Provider And Top Level Domain


"""
#                         Solution



######################## Ass_1 ########################

Name=input("Please Enter Your name : ").strip().capitalize()
print(f"Hello {Name},Happy To See You Here.")

print("="*50)

######################## Ass_2 ########################

age = int(input("Please Enter Your Age : "))
less= age > 16 
message = ["Hello Your Age Is Under 16, Some Articles Is Not Suitable For You",
           f"Hello Your Age Is {age}, All Articles Is Suitable For You"]
print(message[less])

print("="*50)

######################## Ass_3 ########################

first_name = input("Please Enter Your  First Name : ").strip().capitalize()
second_name = input("Please Enter Your Middle Name: ").strip().capitalize()

print(f"Hello {first_name} {second_name:.1s}")

print("="*50)

######################## Ass_4 ########################

Email = input("Please Enter Your Email : ").strip().lower()
user_name = Email[:Email.index('@')].capitalize()
small_name =  Email[Email.index('@')+1:Email.index('.')]
Domain = Email[Email.index('.')+1:]
print(f"Your Name Is {user_name}\nEmail Service Provider Is {small_name}\nTop Level Domain Is {Domain} ")

