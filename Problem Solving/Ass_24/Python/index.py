"""
Problem 1 : Define all the data types that are used in SQLite.

Problem 2 : Create a database file called elzero.db and create a table called users with the following columns: id (integer), name (text), date (text), email (text). Insert the following data into the users table.

Problem 3 : Write a Python function that takes two numbers as parameters and returns their sum. Use type hinting to indicate that the function returns an integer.

Problem 4 : Write a Python function that takes a list of numbers as a parameter and returns the maximum number in the list. Use type hinting to indicate that the function returns an integer.
"""

#                         Solution

############################## Ass_1 ##############################

# NULL	    Represents a NULL value.
# INTEGER	A signed integer, stored in varying byte sizes based on its magnitude.
# REAL	    A floating-point value, stored as an 8-byte IEEE floating point number.
# TEXT	    A text string, stored using the database encoding.
# BLOB	    Binary data, stored exactly as input.

############################## Ass_2 ##############################

import sqlite3

# Create Database File :
db = sqlite3.connect("elzero.db")

# Set Up Curser :
cr = db.cursor()

# Create Users Name , Id , Mail , Date :
cr.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER UNIQUE,
    name TEXT UNIQUE,
    date TEXT UNIQUE,
    email TEXT UNIQUE
)    
 """)

############################## Ass_3 ##############################

# get data :
users_list = [
(1,"Essam","23/08/2005","essammohamed@gmail.com"),
(2,"Amira","17/01/2006","amirahamdy@gmail.com"),
(3,"Omar","23/09/2014","omarmohamed@gmail.com"),
(4,"Sara","1/11/2008","saramohamed@gmail.com"),
(5,"Esraa","5/04/2006","esraakhalid@gmail.com")
]

# Insert Data :
cr.executemany("INSERT OR IGNORE INTO users (id, name, date, email) VALUES (?, ?, ?, ?)", users_list)


############################## Ass_4 ##############################

# Get The Last Row In Table:

# Select Table:
cr.execute("select * from users")

# Result :
result = cr.fetchall()

# Get Last One In Result:
result = cr.fetchall()
if result: 
    print(f"Last Row Is => {result[-1]}")

############################## Ass_5 ##############################

# Input To Delete 
id = input("Please Enter Your Id To Delete : ").strip()

# Select ID From Table:
cr.execute("select id from users")

# Result Of All Id :
result = cr.fetchall()

# Get All Id In List:
ids = []
for row in result:
    ids.append(row[0]) 

if int(id) in ids:
    cr.execute("DELETE FROM users WHERE id = ?", id) # delete User from database
    print("User Deleted.")
    print("Show Other Data")
    cr.execute("select * from users")    # select all users to fetch
    result = cr.fetchall()
    for row in result:
        print(f"ID => {row[0]}, Name => {row[1]}, Date Of Birth => {row[2]}, Email => {row[3]}")
else:
    print("User Not Found.")


db.commit()
db.close()







