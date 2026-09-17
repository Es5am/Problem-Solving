"""
Problem 1 : Get a number from the user and check if it is a single digit number or not. If it is not a single digit number,
raise an IndexError. If the number is 0, raise a ValueError. If the input is not a number, raise an Exception.

Problem 2 : Get a letter from the user and check if it is a single character letter from A to Z. If it is not a single character, raise an IndexError. If the letter is not in the range A to Z, raise a ValueError.

Problem 3 : Create a function called calculate that takes two numbers as parameters and returns their sum. Use type hinting to indicate that the function returns an integer.

"""

#                         Solution


############################## Ass_1 ####################################

NUM = input("Add Your Number : ").strip()


if len(NUM) > 1:

    raise IndexError("Only One Character Allowed")

elif NUM == "0":
    raise ValueError("Number Must Be Larger Than 0")

elif not NUM.isdigit():
    raise Exception("Only Numbers Allowed")


else:
    print(f"The Number Is {NUM}")

print("-"*50)

############################## Ass_2 #################################

LETTER = input("Add Letter From A to Z")

try :
    
    if len(LETTER) > 1:
        raise IndexError
    
    elif "A" <= LETTER <= "Z":
        raise ValueError

except IndexError:
    print("You Must Write One Character Only")


except ValueError:
    print("The Letter Not In A - Z")


else:

    print(f"You Typed {LETTER}")

print("-"*50)

############################## Ass_3 #################################


def calculate(num1, num2)-> int:
  return num1 + num2

print(calculate(20, 30))





















