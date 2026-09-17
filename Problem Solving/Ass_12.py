"""
Problem 1 : Create A Function Called ( calculate ) That Accepts 3 Parameters ( First Number , Second Number , Operation ) And The Default Value Of The Operation Is ( Add ),
Then The Function Should Perform The Required Operation And Return The Result, If The User Didn't Enter The Second Number It Should Be Considered As ( 0 ),
If The User Didn't Enter The Operation It Should Be Considered As ( Add ), If The User Entered An Invalid Operation It Should Print ( Invalid Operator ).

Problem 2 : Create A Function Called ( addition ) That Accepts A Variable Number Of Arguments And Return The Sum Of All Arguments,
But If The User Entered ( 10 ) It Should Be Ignored And If The User Entered ( 5 ) It Should Be Subtracted From The Total Sum.

Problem 3 : Create A Function Called ( skills ) That Accepts A Name And A Variable Number Of Skills,
If The User Didn't Enter Any Skills It Should Print ( Hello {name} You Have No Skills To Show ) And If The User Entered Skills It Should Print ( Hello {name} Your Skills is ) And Print All Skills.

Problem 4 : Create A Function Called ( say_hello ) That Accepts 3 Parameters ( Name , Age , Country ) And The Default Value Of The Name Is ( Unknown ) And 
The Default Value Of The Age Is ( Unknown ) And The Default Value Of The Country Is ( Unknown ).

"""
#                         Solution


################################### Ass_1 ##############################

def calculate(n1,n2=0,calc="Add"):

    calc_for= str(calc).capitalize().strip()
    if calc_for == "Add" or calc_for =="A":
        return f"{n1+n2}"
    elif calc_for == "Subtract" or calc_for =="S":
        return f"{n1-n2}"
    elif calc_for == "Multiply" or calc_for =="M":
        return f"{n1*n2}" 
    elif calc_for == "Division" or calc_for =="D":
        if n2 == 0:
            return "Error : Devision By Zero"
        return f"{n1/n2}"
    else:
        print("Invalid Operator")

print(calculate(10, 20)) 
print(calculate(10, 20, "AdD")) 
print(calculate(10, 20, "a")) 
print(calculate(10, 20, "A")) 

print(calculate(10, 20, "S"))
print(calculate(10, 20, "subTRACT")) 

print(calculate(10, 20, "Multiply"))
print(calculate(10, 20, "m"))

print("="*50)

################################### Ass_2 ##############################


def addition (*numbers):
    total=0
    for num in numbers :
        if num == 10 :
            continue
        if num == 5 :
            total-= 5
        else:
         total+=num
    return total

print(addition(10, 20, 30, 10, 15))
print(addition(10, 20, 30, 10, 15, 5, 100))

print("="*50)

################################### Ass_3 ##############################

def skills (name,*skills):
   
        if not skills:
            print (f"Hello {name} You Have No Skills To Show")
        else :
            print (f"Hello {name} Your Skills is ")
            for skill in skills :
             print(f"- {skill}")
skills("Osama", "HTML", "CSS", "JS", "Python")
skills("Ahmed")

print("="*50)

################################### Ass_4 ##############################

def say_hello(name="Unkown",age="Unkwon",country="Unkown"):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"
print(say_hello("Osama",38,"Egypt"))
print(say_hello())


