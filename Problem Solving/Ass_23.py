"""
Problem 1: Create Game class that has the following attributes: name, developer, year, and price. 
The class should have a method called price_in_pounds that returns the price in Egyptian pounds (1 USD = 15.6 EGP). Create an instance of the Game class and print its details.

Problem 2: Create User class that has the following attributes: fname, mname, age, and gender. The class should have methods called get_name, say_hello, calc_age, and full_details.

Problem 3: Create a Message class that has a static method called print_message that returns "Hello From Class Message". Call the static method without creating an instance of the class.

Problem 4: Create a Games class that has an attribute called item. The class should have a method called show_games 
that prints the number of games or the names of the games based on the type of the item attribute.

Problem 5: Create a Members class that has the following attributes: name and permission. Create two subclasses called Admins and Moderators that inherit from the Members class.
Create instances of both subclasses and print their details.

Problem 6: Create three classes called A, B, and C that have the following attributes: one, two, and three respectively.
Create a class called Text that inherits from all three classes and has a method called show_name that returns the concatenation of the three attributes. Create an instance of the Text class and print its name
"""

#                         Solution

############################## Ass_1 ##############################
      
class Game:

    # Write Class Content 

    def __init__(self,name,developer,year,price):

        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self):

        return f"{self.price * 15.6} Egyptian Pounds"  

game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

print() # -> New line Separetor
print( '-' * 50 ) # -> Separetor



############################## Ass_2 ##############################

class User:

  # Write Class Content

    def __init__(self,fname,mname,age,gender):
      
      self.fname = fname
      self.mname = mname
      self.age = age
      self.gender = gender

    def get_name(self):
        return f"{self.fname} {self.mname[0]}"
    
    def say_hello(self):

        if self.gender == "Male" :
            return f"Hello Mr {self.get_name()}."
        
        elif self.gender == "Female" :
            return f"Hello Mrs {self.get_name()}."
        
        else :
            return f"Hello {self.get_name()}."
    
    def calc_age (self):
        return str(40 - self.age).zfill(2) 
    
    def full_details(self):
        return f"{self.say_hello()} [{self.calc_age()}] Years To Reach 40"
    
    
############################# Ass_2_another_Solution ##############################

    # def full_details(self):
         
    #     if self.gender == "Male" :
    #         return f"Hello Mr {self.fname} {self.mname[0]} .[{str(40-self.age).zfill(2)}] Years To Reach 40"
        
    #     elif self.gender == "Female" :
    #         return f"Hello Mrs {self.fname} {self.mname[0]} .[{str(40-self.age).zfill(2)}] Years To Reach 40"
        
    #     else :
    #         return f"Hello {self.fname} {self.mname[0]} .[{str(40-self.age).zfill(2)}] Years To Reach 40"



user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40

print( '-' * 50 ) # -> Separetor

############################## Ass_3 ##############################

class Message:

  # Write Class Content

  def print_message():
      return "Hello From Class Message"

print(Message.print_message())

# Output
# Hello From Class Message

print( '-' * 50 ) # -> Separetor

############################## Ass_4 ##############################

class Games:

  # Write Class Content

    def __init__(self,item):

        self.item = item

    def show_games(self):

        if type(self.item) == str  :
            print(f"I Have One Game Called \"{self.item}\"")
        
        elif type(self.item) == list :

            print("I Have Many Games:")
            for game in self.item:
                print(f"-- {game}")

        elif type(self.item) == int  :
            print(f"I Have {self.item} Game.")

        else:
            print("Invaild")




my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.


print( '-' * 50 ) # -> Separetor

############################## Ass_5 ##############################

# Main Class
class Members:

  def __init__(self, n, p):

    self.name = n

    self.permission = p

  def show_info(self):

    return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here
class Admins(Members):
    def __init__(self, n, p):
        super().__init__(n, p)

    pass

# Create Moderators Class Here
class Moderators(Admins):
    pass

member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator

print( '-' * 50 ) # -> Separetor

############################## Ass_6 ##############################

class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C:

  def __init__(self, three):

    self.three = three

# Write The Class Called "Name" Here

class Text( A , B , C ):
   
    def __init__(self, one,two,three):
       A.__init__(self,one)
       B.__init__(self,two)
       C.__init__(self,three)

    def show_name(self):
      return f"The Name Is {self.one}{self.two}{self.three}"
    

the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero











